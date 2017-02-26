#coding=utf-8
import urllib
from bs4 import BeautifulSoup as bs
import re
import time
# def match(urls):
# 	pattern = re.compile(r'http')
# 	match = pattern.match(urls)
# 	if match:
# 		print match.group()
#打开链接
def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

#保存读取内容
def savebetter(filename,soup):
	better=soup.prettify("utf-8")
	with open(filename,"a") as file:
		file.write(better)


def savehtml(filename, contents): 
  fh = open(filename, 'a') 
  fh.write(contents) 
  fh.close() 
#找到首页的租房小组列表，获得链接
def FindLinks(soup):
	for link in soup.find_all('a'):
		try:
			url=link.get('href')
			#打开一个租房小组的链接，获得新页面
			nextpage=getHtml(url)
			SecondPage=bs(nextpage,'html.parser')
			#在新页面中找到贴子的链接并打开
			FindLinks_Second(SecondPage)		
		except Exception as e:
			print("can't open FirstPage_title")
			pass


#遍历某个小组的页面，获得发贴的链接
def FindLinks_Second(soup):
	#list-group
	news=soup.find(id="group-topics")
	print("Second_page links")
	for link in news.find_all('a'):
		try:
			url=link.get('href')		
			Thirdpage=getHtml(url)
			Thirdsoup=bs(Thirdpage,'html.parser')
			Third_Soup(Thirdsoup,url)
		except Exception as e:
			print("can't open Secondpage_title")
			continue

#提取贴子楼主发言并保存，保存该页链接
def Third_Soup(soup,url):
	try:
		savehtml('page',"--------------------------------------\n")
		savehtml('page',url)
		title=soup.find(class_="topic-content")
		text=title.find('p')
		savebetter('page',text)
		print("成功提取一位楼主发言")
		time.sleep(5)
	except Exception as e:
		pass



 
url="https://www.douban.com/search?source=suggest&q=北京租房"
html=getHtml(url)
soup=bs(html,'html.parser')

news=soup.find(class_="result-list")
FindLinks(news)

print("over")

# #title
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# # find href in a
# print(soup.a['href'])
