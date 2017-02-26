#coding=utf-8
import urllib
from bs4 import BeautifulSoup as bs
import re
 
# def match(urls):
# 	pattern = re.compile(r'http')
# 	match = pattern.match(urls)
# 	if match:
# 		print match.group()

def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def savehtml(filename, contents): 
  fh = open(filename, 'w',encoding='utf-8') 
  fh.write(contents) 
  fh.close() 

#find all links in a
def FindLinks(soup):
	for link in soup.find_all('a'):
		url=link.get('href')
		nextpage=getHtml(url)
		print(nextpage)

def savebetter(filename,soup):
	better=soup.prettify("utf-8")
	with open(filename,"wb") as file:
		file.write(better)


url="http://www.ifeng.com"

html=getHtml(url)
soup=bs(html,'html.parser')
savebetter("page",soup)


# news=soup.find(id="headLineDefault")

# FindLinks(news)

#save html

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








