# Download amazing pictures from national geographic
from bs4 import BeautifulSoup
import requests
import re
import datetime
import pandas as pd
import os

# 提取第一页至最后一页的url
def get_allpages_url(page_info):
	'''<script>
    var currentPage = 1;
    var baseUrl = 'https://blog.csdn.net/liuchengzimozigreat/article/list' ;
    var pageSize = 20 ;
    var listTotal = 26 ;
    var pageQueryStr = '';
    function getAllUrl(page) {
        return baseUrl + "/" + page + pageQueryStr;
    }
	</script>'''
	# 以上是script_lst[-9]的信息，有三个数：currentPage, pageSize, listTotal  '\d'只查找数字一次，'\d+'则往后查找数字无限次
	currentPage, pageSize, listTotal = [int(num) for num in re.findall(r'\d+', page_info)]
	pageNum = listTotal//pageSize + 1 # 总的网页数
	print('总的网页数:', pageNum, '总的文章数:', listTotal, 'pageSize:', pageSize)
	baseUrl = re.findall(r'\'(.*)\'', page_info)[0] # .*在正则表达式中表示匹配除了'\n'之外的任何字符0次或无限次，在DOTALL中也可以匹配'\n',运行后发现这里就可以
	allpages_url_lst = [baseUrl + '/' + str(page_num) for page_num in range(1, pageNum+1)] # 这里左闭右开，所以总的网页数要+1
	return allpages_url_lst, listTotal

# 获取总体信息
def get_general_info(soup):
	general_info = soup.find('div', {'class': 'data-info d-flex item-tiling'})
	dl_info = general_info.find_all('dl')
	# print(info)
	self_article_num = dl_info[0]['title'] # 原创文章数量
	fans_num = dl_info[1]['title'] # 粉丝数
	like_num = dl_info[2]['title'] # 喜欢数
	comment_num = dl_info[3]['title'] # 评论数
	# print(self_article_num, fans_num, like_num, comment_num)
	return self_article_num, fans_num, like_num, comment_num

# 获取等级信息
def get_grade_info(soup):
	grade_info = soup.find('div', {'class': 'grade-box clearfix'})
	# print(grade_info)
	dd_info = grade_info.find_all('dd')
	grade = dd_info[0].a['title'].split(r',')[0] # 等级
	total_read_num = dd_info[1]['title'] # 总阅读量
	earn_points = dd_info[2]['title'] # 积分
	rank = grade_info.find_all('dl')[-1]['title'] # 排名
	return grade, total_read_num, earn_points, rank

# 返回路径下文件id列表
def eacharticle_id(filepath):
	pathDir =  os.listdir(filepath)  #返回指定路径下所有文件和文件夹的名字,并存放于一个列表中
	id_dict = {}
	for allDir in pathDir:
		article_id = re.findall(r'\d{8}', allDir)
		if len(article_id) != 0:
			id_dict[article_id[0]] = allDir
	return id_dict

if __name__ == '__main__':
	now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	record_time = str(now_time) # 将作为数据存档时间来保存
	date_today = datetime.datetime.now().date() # 今天的时间，将作为文章索引

	URL = "https://blog.csdn.net/liuchengzimozigreat" # 我的blog主页(首页/第一页)

	# find list of image holder
	html = requests.get(URL).text
	soup = BeautifulSoup(html, 'lxml')

	# 提取总体信息
	self_article_num, fans_num, like_num, comment_num = get_general_info(soup)

	# 提取等级信息
	grade, total_read_num, earn_points, rank = get_grade_info(soup)
	

	# 存储总体信息
	file_path = r'H:\learning like never feel tired\Scraping python\my_blog_info' # 存储位置
	general_info_file = file_path + '\\AAA_general_info.csv' # 前面加三个A好让总体信息出现在文件夹第一的位置
	if os.path.exists(general_info_file):
		df = pd.read_csv(general_info_file, index_col=0, engine='python', encoding='utf_8_sig', parse_dates=[0])
	else:
		df = pd.DataFrame(columns=('self_article_num', 'fans_num', 'like_num', 'comment_num', 'grade', 'total_read_num', 'earn_points', 'rank', 'record_time'))
	df.loc[date_today] = [self_article_num, fans_num, like_num, comment_num, grade, total_read_num, earn_points, rank, record_time] # 用当天日期作为索引,更新信息
	df.to_csv(general_info_file, encoding='utf_8_sig')


	# 提取各个文章的信息
	script_lst = soup.find_all('script') # 提取其中的script标签tag，其中script_lst[-9]含有listtotal和pagesize信息
	allpages_url_lst, total_article_num = get_allpages_url(str(script_lst[-9])) # 提取各page的url

	page_article_lst = [] # 存储所有网页中article集合的信息
	for page_url in allpages_url_lst:
		html = requests.get(page_url).text
		soup = BeautifulSoup(html, 'lxml')
		article_info = soup.find_all('div', {'class': 'article-item-box csdn-tracking-statistics'})
		page_article_lst.append(article_info)
		# print(type(article_info))

	article_info_lst = [] # 将所有文章整合进同一个列表中
	for elem in page_article_lst:
		mark = 0
		for article in elem:
			if mark == 0: # 查看HTML发现每一页中都会在最开头的地方多一篇未显示的文章'帝都的凛冬'
				mark = 1
				continue
			article_info_lst.append(article)

	# 提取文章属性并保存之，将保存八个信息：文章信息记录的日期——作为索引、文章名、文章类型、创建时间、阅读量、评论量、文章url、该条记录时间(精确到秒)
	id_dict = eacharticle_id(file_path) # 有时文章名字改了，但文章id不变
	# print(len(id_dict))
	for article in article_info_lst:
		# print(article)
		span = article.find_all('span') # span包含了四个属性，依次是：article_type, date, read_num, comment_num
		article_type = re.split(r'\s*', str(span[0]))[3] # 文章类型
		create_date = span[1].get_text() # 创建时间
		read_num = re.sub(r'\D*', '', span[2].get_text()) # 阅读数
		print(read_num)
		comment_num = span[3].get_text() # 评论数

		article_url = article.a['href'] # 文章链接
		article_id = re.split(r'/', article_url)[-1] # url中最后一部分是文章id
		print(article_id)
		# 用'\n'分割结果类似：['', '    原    ', '    linux命令学习汇总      ']，需将最后一个字符串左右两边空格去掉才是我们想要的结果
		# 用' {2,}'——空格2到无限次分割结果类似：['', 'rails官方指南--建一个简易博客', '']，因此去列表中的第二个作为我们的article_name
		article_name = re.split(r' {2,}', re.split(r'\n*', str(article.find('a').get_text()))[-1])[1] # 文章名称  当时我还不知道，其实换成re.sub()更好

		if article_id in list(id_dict.keys()): # 通过id判断
			print('old article:', id_dict[article_id])
			df = pd.read_csv(file_path + '\\' + id_dict[article_id], parse_dates=[0], index_col=0, engine='python', encoding='utf_8_sig') # 有时难免程序在一天内多次运行，读入数据是保证一天只记录一个数据
			os.remove(file_path + '\\' + id_dict[article_id]) # 删除旧文章信息，因为文章名字可能改了
		else:
			print('NEW ARTICLE:', article_name)
			df = pd.DataFrame(columns=('article_id', 'article_name', 'article_type', 'create_date', 'read_num', 'comment_num', 'article_url', 'record_time'))
		df.loc[date_today] = ['article_id', article_name, article_type, create_date, read_num, comment_num, article_url, record_time] # 用当天日期作为索引，更新信息

		file_name = re.sub(r'[\s\':,\.()，-]*', '', article_name) # 将文章名字中那些非正经字符删除
		file = file_path + '\\' + article_id + re.findall(r'\w{2,20}', file_name)[0] + '.csv' # 文件名不宜太长，所以最多取20个\w——单词字符[A-Za-z0-9]，过短又会冲突
		df.to_csv(file, encoding='utf_8_sig')

# 下面是一些HTML目标模块的信息，也就这些信息，才能提炼出你想要的结果
'''
# 每个article的原始信息
<div class="article-item-box csdn-tracking-statistics" data-articleid="78773093">
<h4 class="">
<a href="https://blog.csdn.net/liuchengzimozigreat/article/details/78773093" target="_blank">
<span class="article-type type-2">
            转        </span>
        postgresql数据库常用操作命令及SQL语言      </a>
</h4>
<p class="content">
<a href="https://blog.csdn.net/liuchengzimozigreat/article/details/78773093" target="_blank">
        环境ubuntu,安装了postgresql
截屏命令：shift+PrtSc可以有十字光标，任选截屏区域
               alt+PrtSc截取当前活动窗口
               PrtSc截取整个屏幕

1postgresql常用操作：
（1）登录
peng@peng-v...      </a>
</p>
<div class="info-box d-flex align-content-center">
<p>
<span class="date">2017-12-11 16:10:49</span>
</p>
<p>
<span class="read-num">阅读数：914</span>
</p>
<p>
<span class="read-num">评论数：0</span>
</p>
</div>
</div>
'''

'''
# general_info的信息，包含原创、粉丝、喜欢、评论
<div class="data-info d-flex item-tiling">
<dl class="text-center" title="22">
<dt><a href="https://blog.csdn.net/liuchengzimozigreat?t=1">原创</a></dt>
<dd><a href="https://blog.csdn.net/liuchengzimozigreat?t=1"><span class="count">22</span></a></dd>
</dl>
<dl class="text-center" id="fanBox" title="2">
<dt>粉丝</dt>
<dd><span class="count" id="fan">2</span></dd>
</dl>
<dl class="text-center" title="5">
<dt>喜欢</dt>
<dd><span class="count">5</span></dd>
</dl>
<dl class="text-center" title="4">
<dt>评论</dt>
<dd><span class="count">4</span></dd>
</dl>
</div>
'''

'''
<div class="grade-box clearfix">
<dl>
<dt>等级：</dt>
<dd>
<a href="https://blog.csdn.net/home/help.html#level" target="_blank" title="2级,点击查看等级说明">
<svg aria-hidden="true" class="icon icon-level">
<use xlink:href="#csdnc-bloglevel-2"></use>
</svg>
</a>
</dd>
</dl>
<dl>
<dt>访问：</dt>
<dd title="7462">
                7462            </dd>
</dl>
<dl>
<dt>积分：</dt>
<dd title="304">
                304            </dd>
</dl>
<dl title="289473">
<dt>排名：</dt>
<dd>28万+</dd>
</dl>
</div>
'''
