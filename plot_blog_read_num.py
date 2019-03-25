

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
# created on 2019/3/5
# @author: liucheng
# python 3.6.6    win10
# sublime text
# discription: this program is to conduct statistics on result of MK test, so as to find out
			the number of each kind of ID(station)
'''


import pandas as pd
import pylab as plt
import sys
import os
import re
import datetime
plt.rcParams['font.sans-serif']=['SimHei']  # 解决图中中文乱码问题

# get files in filepath
def get_file(filepath):
    pathDir =  os.listdir(filepath)  #返回指定路径下所有文件和文件夹的名字,并存放于一个列表中
    return pathDir

# complement missing data in the file
def complement_file(dates, df):
	new_df = pd.DataFrame(columns=['date']) # new_df中只有完整时间序列
	# print(df)
	new_df.iloc[:, 0] = dates  # 将完整时间序列给new_df
	# print(new_df)
	new_df = pd.merge(new_df, df, how='left', on=['date']) # 将含有不完整read_num信息的df与new_df合并，这样new_df含有了完整时间序列和不完整的read_num序列
	# print(new_df.dtypes
	new_df = new_df.interpolate()  # 对其进行插值，插值是线性的，插值结果是补全了read_num序列
	new_df.read_num = new_df['read_num'].astype(int) # 将read_num序列设为int类型
	# print(new_df)
	return new_df


# 每个文件制定好需要的数据
def get_ready_and_plot_file(path):
	files = get_file(path) # 获取所有文章信息的文件名
	print(files)

	for file in files:
		# if not re.match('AAA', file): #
		# 	continue
		df = pd.read_csv(path+'\\'+file, engine='python', encoding='utf-8-sig', parse_dates=[0]) # 传入字典是解析该列并命名为date
		print(file)
		dates = pd.date_range(df.iloc[0, 0], df.iloc[-1, 0]) # 获取各个文章起始时间，并生成完整时间序列
		if len(dates) == df.index.size: # 如果起始时间长度和文章记录长度一致，就跳过，不需补全
			continue
		complete_df = complement_file(dates, df.loc[:, ('date', 'read_num')]) # 只需要时间和阅读数两列信息就好了
		print(complete_df)
		plt.plot(complete_df.date, complete_df.read_num)
		if re.match('AAA', file):
			plt.title('General information', size=15)
		else:
			plt.title(df.article_name[0])
		plt.ylabel('read_num', size=20, color='red') 
		plt.xlabel('date', size=20, color='deepskyblue')
		plt.xticks(rotation=45)
		plt.grid(axis='y')
		plt.show()
		


# 画出每个文件中的阅读数
def plot_read_num():
	path = r'H:\learning like never feel tired\Scraping python\my_blog_info'
	get_ready_and_plot_file(path)

	

# 有时文章信息不对，这里来改正之
def correct_article_info():
	path = r'H:\learning like never feel tired\Scraping python\my_blog_info'

	file_lst = get_file(path)

	for file in file_lst:
		if re.match('AAA', file):
			continue
		df = pd.read_csv(path+'\\'+file, engine='python', encoding='utf-8-sig', parse_dates=[0], index_col=0) # 传入字典是解析该列并命名为date
		print(len(df.columns))
		# df.read_num = df['read_num'].astype(str) # 如果不重新赋值的话，那么原dataframe中该列就没有变
		# df.comment_num = df['comment_num'].astype(str)
		# print(df.dtypes)
		# df.read_num = [int(re.sub(r'\D*', '', elem)) for elem in df.read_num]
		# df.comment_num = [int(re.sub(r'\D*', '', elem)) for elem in df.comment_num]
		df.article_id = [df.article_id[len(df.article_id)-1]]*len(df.article_id)
		print(df)
		if len(df.columns) == 9:
			df.to_csv(path+'\\'+file, encoding='utf_8_sig', index=False)
		else:
			df.to_csv(path+'\\'+file, encoding='utf_8_sig')





if __name__ == '__main__':
	# correct_article_info()
	plot_read_num()





	