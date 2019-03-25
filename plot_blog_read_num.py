

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

# get files in filepath
def get_file(filepath):
    pathDir =  os.listdir(filepath)  #返回指定路径下所有文件和文件夹的名字,并存放于一个列表中
    return pathDir

# complement missing data in the file
def complement_file(dates, df):
	new_df = pd.DataFrame(columns=['date'])
	# new_df.iloc[:, 0] = dates
	# new_df = pd.merge(new_df, df, how='left', on=['date'])
	# df.resample('D', on='date').mean()

	print(df.columns)


if __name__ == '__main__':
	path = r'H:\learning like never feel tired\Scraping python\my_blog_info'

	files = get_file(path)
	print(files)


	for file in files:
		if re.match('AAA', file):
			df = pd.read_csv(path+'\\'+file, engine='python', encoding='utf-8-sig', parse_dates={'date':[0]})
			continue
		df = pd.read_csv(path+'\\'+file, engine='python', encoding='utf-8-sig', parse_dates={'date':[0]}) # 传入字典是解析该列并命名为date
		df.read_num = [int(re.sub(r'\D*', '', elem)) for elem in df.read_num]
		print(df.iloc[:, -4:-1])
		df.to_csv(path+'\\'+file, encoding='utf_8_sig')


		# df = pd.read_csv(path+'\\'+file, engine='python', encoding='utf-8-sig', parse_dates={'date':[0]}) # 传入字典是解析该列并命名为date
		# print(df.read_num)
		# dates = pd.date_range(df.iloc[0, 0], df.iloc[-1, 0]) # 获取各个文章起始时间，并生成完整时间序列
		# if len(dates) == df.index.size: # 如果起始时间长度和文章记录长度一致，就跳过，不需补全
		# 	continue

		# complete_df = complement_file(dates, df)