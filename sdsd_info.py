#coding=UTF-8
'''
Created on 2016年4月27日

@author: Feng Yujie
'''
import urllib2
from bs4 import BeautifulSoup
import re
url='http://www.view.sdu.edu.cn/'

response=urllib2.urlopen(url)
if response.getcode()==200:
    html_cont=response.read()
    soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    links=soup.find_all('a')
    count=0
    pattern=re.compile(r'http')
    for link in links:
        count=count+1
        img=link.find('img')
        if img!=None:
            if pattern.match(link['href']):
                if img.find('alt'):
                    print 'link%d'%count,link['href'],img['alt']
                else:
                    print 'link%d'%count,link['href']
        else:
            if pattern.match(link['href']):
                print 'link%d'%count,link['href'],link.get_text()
                if link.get_text()==None:
                    if link.find('title'):
                        print link['title']
            else:
                print 'link%d'%count,'http://sdu.edu.cn/'+link['href'],link.get_text()
                if link.get_text()==None:
                    if link.find('title'):
                        print link['title']