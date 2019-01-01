# 爬取国科大2017级研究生公开招考录取名单
from bs4 import BeautifulSoup
import requests
import re
import datetime
import pandas as pd
import os

def get_admission_info(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')

	df = pd.DataFrame(columns=('院系所代码', '姓名', '拟录取专业名称', '复试成绩'))
	admission_tr = soup.find_all('tr')
	for i,student in enumerate(admission_tr):
		student_info = re.split(r'\n', str(student.text))
		student_info = [student_info[1], student_info[2], student_info[3], student_info[4]]
		if i == 0:
			continue
		else:
			df.loc[i] = student_info
		# print(student_info)
	# print(df)
	return df


def get_institute_info(url):
	html = requests.get(url).text	
	soup = BeautifulSoup(html, 'lxml')
	# print(soup)

	# table = soup.find_all('table', {'border':'1'})
	# institute_tr = table[0].find_all('tr')
	institute_tr = soup.find_all('tr')
	# print(institute_tr)
	
	cnt = 0
	# print(len(institute_tr))
	df = pd.DataFrame(columns=('招生单位代码', '招生单位名称', '院系所代码', '院系所名称'))
	for institute in institute_tr:
		lst1 = re.split(r'\n', str(institute.text))
		if len(lst1) != 14: # 有其他不符的信息，删除之
			continue
		lst = []
		for elem in lst1:
			if elem != '':
				lst.append(elem)
		if len(lst) != 4: # 有其他不符的信息，删除之
			continue
		if cnt == 0: # 符合的信息中第一列是：'招生单位代码', '招生单位名称', '院系所代码', '院系所名称'，  因此不加入df
			cnt = 1
			continue
		df.loc[cnt] = lst
		cnt = cnt + 1
	# print(df)
	return df

import pandas as pd
def statistics_of_family_name():
	file = r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\2017_UCAS_Admission_list.csv'
	df = pd.read_csv(file, index_col=0, engine='python', encoding='utf_8_sig')
	# print(df)
	df['姓'] = [name[0] for name in list(df.loc[:, '姓名'])]
	a=df.groupby(['姓']).size()
	df1 = pd.DataFrame(a, index=a.index, columns=['人数'])
	df1['百分比']=[str(round(pct*100, 3)) + '%' for pct in df1.iloc[:,0]/a.sum()]
	df2 = df1.sort_values(by='人数', ascending=False)
	# print(df2)
	file = r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\2017_UCAS_student_family_name.csv'
	# df2.to_csv(file, encoding='utf_8_sig')

	institute_g = df.groupby(['院系所代码', '院系所名称'], as_index=False).size().reset_index()
	institute_g.rename(columns={0:'人数'}, inplace = True)
	print(institute_g)
	institute_g['人数占比']=[str(round(pct*100, 2)) + '%' for pct in institute_g.iloc[:,2]/institute_g.人数.sum()]
	institute_g_sorted = institute_g.sort_values(by='人数', ascending=False)
	print(institute_g_sorted.index.size)
	institute_g_sorted['人数排名'] = [i for i in range(1,128)]
	file = r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\2017_UCAS_student_num_each_inst.csv'
	institute_g_sorted.to_csv(file, index=False, encoding='utf_8_sig')
	print(institute_g_sorted)


	# print(a/a.sum())
	# print(a.sort_values(ascending=False))
	# print(a.index)
	# print(a.sort_values(by=0, axis=1))

# 推免生信息
def get_rec_student_info(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'lxml')
	# print(soup)

	df = pd.DataFrame(columns=('院系所代码', '姓名', '录取专业名称', '复试成绩', '招生类型名称'))
	admission_tr = soup.find_all('tr')
	print(len(admission_tr))
	for i,student in enumerate(admission_tr):
		# print(student.text)
		student_info = re.split(r'\n', str(student.text))
		# print(student_info)
		student_info = [student_info[1], student_info[2], student_info[3], student_info[4], student_info[5]]
		if i == 0:
			continue
		else:
			df.loc[i] = student_info
		# print(student_info)
	print(df)
	file = r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\2018_UCAS_Admission_rcm.csv'
	df.to_csv(file, encoding='utf_8_sig')
	# return df




if __name__ == '__main__':
	# now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# record_time = str(now_time) # 将作为数据存档时间来保存
	# date_today = datetime.datetime.now().date() # 今天的时间，将作为文章索引
	# print(date_today, record_time)

	# 录取信息
	addmission_lst_URL = "http://admission.ucas.edu.cn/showarticle/Article/4c7e0e9f-2311-47a0-8f12-b0ec992078ac/7a5c35a4-0d9d-4918-ac7e-21af8dbd11c3"
	# # 院系信息
	institute_lst_URL = 'http://www.ipeedu.com/masterAdmission/8338.jhtml'

	# 2018推免生
	addmission_rcm_URL = "http://admission.ucas.ac.cn/showarticle/article/4c7e0e9f-2311-47a0-8f12-b0ec992078ac/26651774-b9eb-4399-9b44-3acbc90e2d34"


	institute_df = get_institute_info(institute_lst_URL)
	institute_df.to_csv(r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\institute_info.csv', encoding='utf_8_sig')

	# addmission_rcm_df = get_rec_student_info(addmission_rcm_URL)

	# admission_df = get_admission_info(addmission_lst_URL)

	# df_merge = pd.merge(admission_df, institute_df, on='院系所代码', how='left')
	# file = r'H:\learning like never feel tired\Scraping python\2017UCAS_admission_info\2017_UCAS_Admission_list.csv'
	# df_merge.to_csv(file, encoding='utf_8_sig')

	# 统计各个姓氏占比排名
	# statistics_of_family_name()






	

	

	

	
