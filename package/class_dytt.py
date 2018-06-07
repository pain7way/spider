# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import re


class Dytt:
    
    def __init__(self):
        self.h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
        self.dy2018 = []
        self.dytt8 = []

    def dy2018_movie(self):
        self.dy2018 = []
        url = 'https://www.dy2018.com/'
        try:
            r = requests.get(url, timeout=5, headers=self.h)
            r.encoding = 'gbk'
            bs = BeautifulSoup(r.text, 'lxml')
            a = bs.find_all('div', class_='co_content222')
            for i in a[0].find_all('li'):
                self.dy2018.append(i.text)
#                print(i.text)
            self.dy2018.append('---------------------------------------------')
#            print('\n')
            for j in a[2].find_all('li'):
                self.dy2018.append(j.text)
#                print(j.text)
            return self.dy2018
        except requests.exceptions.RequestException:
            time.sleep(1)
            return self.dy2018_movie()


    def dytt8_movie(self):
        self.dytt8 = []
        url = 'http://www.dytt8.net/'
        try:
            r = requests.get(url, timeout=5, headers=self.h)
            r.encoding = 'gbk'
            bs = BeautifulSoup(r.text, 'lxml')
            a = bs.find_all('div', class_='co_content8')
            href1 = re.compile('\/html\/gndy\/dyzz\/[0-9]*\/[0-9]*\.html')
            for i in a[0].find_all('a', href=re.compile(href1)):
#                print(i.text)
                self.dytt8.append(i.text)
            self.dytt8.append('---------------------------------------------')
#            print('\n')
            href2=re.compile('\/html\/gndy\/jddy\/[0-9]*\/[0-9]*\.html')
            for j in a[1].find_all('a', href=re.compile(href2)):
#                print(j.text)
                self.dytt8.append(j.text)
            return self.dytt8
        except requests.exceptions.RequestException:
            time.sleep(1)
            return self.dytt8_movie()



