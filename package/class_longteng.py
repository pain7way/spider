# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

class LongTeng:
    
    def __init__(self):
        self.h ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Encoding':'gzip, deflate, sdch',
                 'Accept-Language':'zh-CN,zh;q=0.8',
                 'Referer':'http://www.ltaaa.com/',
                 'Upgrade-Insecure-Requests':'1',
                 'Cache-Control':'max-age=0',
                 'Connection':'keep-alive',
                 'Host':'www.ltaaa.com'
                 }
        self.longteng_list = []
        self.longteng_list_url = []

    def longteng_lists(self):
        self.longteng_list = []
        self.longteng_list_url = []
        longteng_url = 'http://www.ltaaa.com/'
        req = requests.get(longteng_url, headers = self.h, timeout=5)
        bs = BeautifulSoup(req.text, 'lxml')      
        for i in bs.findAll('h2'):
            for j in i.findAll('a', target = '_blank'):
                try:
                    longteng_coin = '['+j.find('label').text+']' 
                    self.longteng_list.append(longteng_coin+j.attrs['title'])
                except AttributeError:
                    self.longteng_list.append(j.attrs['title'])           
        for i in bs.findAll('h2'):
            for j in i.findAll('a', target = '_blank'):
                self.longteng_list_url.append(j.attrs['href'])
        return self.longteng_list

    def read_longteng(self, x):
        num = self.longteng_list.index(x)
        url_one_timu = self.longteng_list_url[num]    
        url_one_timu = 'http://www.ltaaa.com/'+url_one_timu
        req = requests.get(url_one_timu, headers = self.h, timeout=5)
        bsobj = BeautifulSoup(req.text, 'lxml')   
        print('\n-- 译文简介 --\n')
        print(bsobj.find('strong').text.replace(' ', '')+'\n')
        print(bsobj.find('div', class_ = 'post-description').text)
        print('\n-- 正文翻译 --\n')
        print(bsobj.find('div',class_='post-content').text.replace('<br/>',''))
        print('\n-- 评论翻译 --\n')
        print(bsobj.find('div',class_='post-comment').text.replace('<br/>',''))


