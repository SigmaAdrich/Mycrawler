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

def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html


def savebetter(filename,soup):
	better=soup.prettify("utf-8")
	with open(filename,"a") as file:
		file.write(better)

#find all links in a in First Page
def FindLinks(soup):
	for link in soup.find_all('a'):
		try:
			url=link.get('href')
			print(url)
			nextpage=getHtml(url)
			SecondPage=bs(nextpage,'html.parser')
			FindLinks_Second(SecondPage)		
		except Exception as e:
			print("can't open FirstPage_title")
			pass


#find all links in a in Second Page
def FindLinks_Second(soup):
	#list-group
	news=soup.find(id="group-topics")
	print("Second_page links")
	for link in news.find_all('a'):
		try:
			url=link.get('href')
			print(url)
			Thirdpage=getHtml(url)
			print("Thirdpage success")
			Thirdsoup=bs(Thirdpage,'html.parser')
			print("Thirdsoup success")
			Third_Soup(Thirdsoup)
		except Exception as e:
			print("can't open Secondpage_title")
			continue


def Third_Soup(soup):
	try:
		title=soup.find(class_="topic-content")
		text=title.find('p')
		print(text)
		savebetter('page',text)
		time.sleep(5)
	except Exception as e:
		pass



 
url="https://www.douban.com/search?source=suggest&q=北京"

html=getHtml(url)
soup=bs(html,'html.parser')
print(soup)

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
