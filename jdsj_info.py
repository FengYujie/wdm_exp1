#coding:utf-8
'''
Created on 2016年5月8日

@author: Feng Yujie
'''
import urllib2
from bs4 import BeautifulSoup
import re

root_url='http://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8k7efomi.57bjs'
response=urllib2.urlopen(root_url)
if response.getcode()!=200:
    print 'visit failed'
else:
    html_cont=response.read()
    soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    #<div id="J_goodsList" class="goods-list-v1 gl-type-3 J-goods-list"><ul class="gl-warp clearfix" data-tpl="3"><li data-sku="1861098" data-spu="1861091" class="gl-item">
    goodlist=soup.find('div',id="J_goodsList")
    goods=goodlist.find_all('li',class_=re.compile("gl-item"))
    count=1
    good_c=0
    for good in goods:
        good_c=good_c+1
        print 'goodcount:',good_c,good
        p_name=good.find('div',class_=re.compile("p-name"))
        p_price=good.find('div',class_=re.compile("p-price"))
        #print p_name
        if p_name!=None and  p_price!=None:
            link=p_name.find('a',href=re.compile(r'//item.jd.com/\d+.html'))
            if link!=None:
                print 'link%d'%count,'http:'+link['href'],'\ntitle:',link.get_text(),'\nprice:',p_price.get_text()
                count=count+1