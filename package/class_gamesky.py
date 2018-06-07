# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class Gamesky:


    def __init__(self):
        self.h ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                 'Accept-Encoding':'gzip, deflate, sdch',
                 'Accept-Language':'zh-CN,zh;q=0.8',
                 'Cache-Control':'max-age=0',
                 'Connection':'keep-alive',
                 'Upgrade-Insecure-Requests':'1',
                 'Host':'www.gamersky.com'
                 }
        self.gamesky_list = []
        self.gamesky_url = 'http://www.gamersky.com/'

    def get_gamesky(self):
        self.gamesky_list = []        
        r = requests.get(self.gamesky_url, headers=self.h , timeout=5)
        r.encoding = 'utf8'
        bs = BeautifulSoup(r.text, 'lxml')
        for i in bs.find('ul', class_='Ptxt block').findAll('li', class_ = 'li3'):
            self.gamesky_list.append(i.find('a').attrs['title'])
#        for i in self.gamesky_list:
#            print(i)
        return self.gamesky_list