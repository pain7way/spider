# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

class LoL:

    def __init__(self):
        self.h = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Cookie':'UM_distinctid=160db9226eb2b6-021c81b883b75d-2b6f686a-1fa400-160db9226ed3ad; CNZZDATA1256638919=1988022604-1515511238-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1515511238; CNZZDATA1256638869=211400056-1515987248-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1517196226; ngaPassportUid=20360976; ngaPassportUrlencodedUname=%25C0%25CF%25C4%25CF%25B9%25CF%25BA%25A3; ngaPassportCid=Z8id6f7ko83iefona7gnqn8c0t9il88ev99safbm; CNZZDATA1256638874=1756699504-1515989236-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1517372713; ngacn0comUserInfo=%25C0%25CF%25C4%25CF%25B9%25CF%25BA%25A3%09%25E8%2580%2581%25E5%258D%2597%25E7%2593%259C%25E6%25B5%25B7%0939%0939%09%0910%090%094%090%090%09; ngacn0comUserInfoCheck=ed102a2f8d4e63f270de8e8355520042; ngacn0comInfoCheckTime=1517379426; lastvisit=1517379434; lastpath=/read.php?tid=13368894; bbsmisccookies=%7B%7D; CNZZDATA1256638858=1965554525-1515510180-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1517374849; CNZZDATA30043604=cnzz_eid%3D1331512893-1515509734-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1517376525; CNZZDATA30039253=cnzz_eid%3D2136686400-1515509702-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1517376323',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                  'Accept-Encoding':'gzip, deflate, sdch',
                  'Accept-Language':'zh-CN,zh;q=0.8',
                  'Cache-Control':'max-age=0',
                  'Connection':'keep-alive',
                  'Host':'bbs.nga.cn',
                  'Upgrade-Insecure-Requests':'1'
                  }
        self.lol_list = []
        self.lol_dic = pd.DataFrame()

    def lol_lists(self):
        self.lol_list = []
        self.lol_dic = {}
        lol_url = 'http://bbs.nga.cn/thread.php?fid=-152678&rand=132'
        r = requests.get(lol_url, headers = self.h, timeout = 5)
        r.encoding = 'gbk'
        bsh = BeautifulSoup(r.text, 'lxml')
        for i in bsh.findAll('td', class_ = 'c2'):
            self.lol_list.append(i.text.replace('\n', ''))
            self.lol_dic[i.text.replace('\n', '')] = i.a.attrs['href']
        self.lol_dic = pd.DataFrame.from_dict(self.lol_dic, orient = 'index')
        self.lol_dic = self.lol_dic.reset_index(drop = False)
        self.lol_dic.columns = ['题目', '链接']
        return self.lol_list
    
    def read_lol(self, x, num):
        y = self.lol_dic.iloc[list(self.lol_dic['题目']).index(x), 1]
        url = 'http://bbs.ngacn.cc'+y+'&page='+str(num)
        nga_html = requests.get(url, headers = self.h, timeout=5)
        nga_html.encoding = 'gbk'
        nga_bs = BeautifulSoup(nga_html.text, 'lxml')
        try:
            qqq = nga_bs.find('p', {'id':re.compile('postcontent\d*')},
                                    class_=re.compile('postcontent ubbcode'))
            print('\n' + x + '\n')
            for i in qqq.strings:
                print(i)
            print('\n')
        except AttributeError:
            None
        print('-- 第'+str(num)+'页 -- \n')
        qwe = nga_bs.findAll('span', {'id':re.compile('postcontent\d*')},
                                      class_=re.compile('postcontent ubbcode'))
        qqq = nga_bs.findAll('table',class_="forumbox postbox")
        for i in qwe:
            reply = i.text
            reply = reply.replace('[/b]','[/b]\n')
            reply = reply.replace('[quote]','回复')        
            reply = reply.replace('[/quote]','\n回复\n')
            reply = re.sub('\[(.*?)\]','!@#$',reply)
            reply = reply.replace('!@#$','')
            reply = reply.replace('回复','')
            reply = re.sub('Reply.*by','回复:',reply)
            print(reply + '\n\n')
        print('-- 第' + str(num) + '页 --')



