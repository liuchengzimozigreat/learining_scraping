# Download amazing pictures from national geographic
from bs4 import BeautifulSoup
import requests
import re
import datetime
import pandas as pd
import os

def getChapterURL(soup):
	divContainURL = soup.find('div', {'class':'menu-new-lh-menu-container'})
	liContainURL = divContainURL.find_all('li')
	print(liContainURL[0].a['href'])
	urlList = []
	for li in liContainURL:
		urlList.append(li.a['href'])
	print(urlList)
	return urlList

def getChapterInfo(url):
	html = requests.get(url).text
	# soup = BeautifulSoup(html, 'lxml')

	divContent = soup.find('div', {'class': 'column column-content single'})
	print(divContent)
	return html




if __name__ == '__main__':
	URL = "http://www.phrasebank.manchester.ac.uk/" # 我的blog主页(首页/第一页)

	# find list of image holder
	html = requests.get(URL).text
	soup = BeautifulSoup(html, 'lxml')
	print(soup)

	urlList = getChapterURL(soup)

	for url in urlList:
		# print(url)
		print(re.split(r'\/', url)[-2])
		urlHtml = getChapterInfo(url)
		# print(urlHtml)
		with open(r'F:\learning like never feel tired\learning_scraping\academic phrasebank\\' + re.split(r'\/', url)[-2] + '.html','w', encoding="utf-8") as f:
			f.write(urlHtml)
		# break
	

