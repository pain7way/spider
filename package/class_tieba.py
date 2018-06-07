# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

class TieBa:
    def __init__(self):
        self.h ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        self.dic_url_title = {}
        self.list_title = []


    def tieba(self, keyword):
        self.dic_url_title = {}
        self.list_title = []
        url = 'http://tieba.baidu.com/f?kw=' + keyword
        r = requests.get(url, timeout=5, headers=self.h)
        bs = BeautifulSoup(r.text,'lxml')
        title_ = bs.find_all('a',rel="noreferrer",href=re.compile('/p/.*'),class_="j_th_tit")
        for i in title_:
            self.dic_url_title[i.get('href')]=i.get('title')
            self.list_title.append(i.get('title'))
        return self.list_title


    def read_tieba(self, title, page_num):
        url = list(self.dic_url_title.keys())[list(self.dic_url_title.values()).index(title)]
        url = 'http://tieba.baidu.com'+url+'?pn='+str(page_num)
        r = requests.get(url, timeout=5, headers=self.h)
        bs = BeautifulSoup(r.text,'lxml')
        print(title+'\n')
        try:
            username = bs.find('div',class_="l_post j_l_post l_post_bright noborder ").find('div',class_="louzhubiaoshi j_louzhubiaoshi").get('author')
            content = bs.find('div',class_="d_post_content j_d_post_content clearfix").text
            print('楼主:'+username+':')
            print(content.replace(' ','')+'\n')
            for i in bs.find_all('div',class_="l_post j_l_post l_post_bright "):
                username = i.find('img',username=re.compile('.*')).get('username')
                content = i.find('div',class_="d_post_content j_d_post_content clearfix").text
                print(username+':')
                print(content.replace(' ','')+'\n\n')
        except AttributeError:
            print('共' + str(page_num) + '页')

if __name__=='__main__':
    tb = TieBa()
    list_tieba = tb.tieba('macbookpro')
    tb.read_tieba('MBP吧【广告交易帖】，短期内不再单月开贴，持续置顶....',1)
