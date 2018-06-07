# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

class Douban:

    def __init__(self):
        self.h={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding':'gzip, deflate, sdch, br',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Cookie':'ll="108288"; bid=1oQ03kHmWt4; gr_user_id=9f42bcec-d1bb-4a0c-a046-05d70ce8f552; _ga=GA1.2.304494281.1515647254; viewed="1142794_5390209_1825593_1921937_26969886_25919764"; ct=y; dbcl2="120699084:a3imORmG5Ew"; ck=7NLM; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1524446793%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dk8VI2acyGGuBEgHWaX8wiOUXQa25Kx4hr-ZjkPGmLRL05_8LMqQWQ_eEuokavmfrssoPp0sT4nXLzE4HJFA5_YJYEtzreW8CXUNN0DVgPOm%26wd%3D%26eqid%3De6661c170001db84000000025add3646%22%5D; __utma=223695111.1661074626.1515647254.1524204481.1524446794.79; __utmb=223695111.0.10.1524446794; __utmc=223695111; __utmz=223695111.1524446794.79.70.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=01F3CAF7ADEC8BDF7B9D28BDB9C8AD92|68772523a3d2551855d4f3c5701ebce8; _pk_id.100001.4cf6=74a645990feaec8d.1515647254.76.1524448674.1524204481.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utma=30149280.304494281.1515647254.1524204481.1524446793.128; __utmb=30149280.20.10.1524446793; __utmc=30149280; __utmz=30149280.1524446793.128.119.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.12069; ap=1',
                'Host':'api.douban.com',
                'Referer':'https://movie.douban.com/',
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                }
        self.h2={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Encoding':'gzip, deflate, sdch, br',
                 'Accept-Language':'zh-CN,zh;q=0.8',
                 'ache-Control':'max-age=0',
                 'Connection':'keep-alive',
                 'Cookie':'ll="108288"; bid=1oQ03kHmWt4; gr_user_id=9f42bcec-d1bb-4a0c-a046-05d70ce8f552; _ga=GA1.2.304494281.1515647254; viewed="1142794_5390209_1825593_1921937_26969886_25919764"; ct=y; dbcl2="120699084:a3imORmG5Ew"; ck=7NLM; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1524446793%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dk8VI2acyGGuBEgHWaX8wiOUXQa25Kx4hr-ZjkPGmLRL05_8LMqQWQ_eEuokavmfrssoPp0sT4nXLzE4HJFA5_YJYEtzreW8CXUNN0DVgPOm%26wd%3D%26eqid%3De6661c170001db84000000025add3646%22%5D; __utma=223695111.1661074626.1515647254.1524204481.1524446794.79; __utmb=223695111.0.10.1524446794; __utmc=223695111; __utmz=223695111.1524446794.79.70.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=01F3CAF7ADEC8BDF7B9D28BDB9C8AD92|68772523a3d2551855d4f3c5701ebce8; _pk_id.100001.4cf6=74a645990feaec8d.1515647254.76.1524448674.1524204481.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utma=30149280.304494281.1515647254.1524204481.1524446793.128; __utmb=30149280.20.10.1524446793; __utmc=30149280; __utmz=30149280.1524446793.128.119.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.12069; ap=1',
                 'Host':'movie.douban.com',
                 'Referer':'https://movie.douban.com/',
                 'Upgrade-Insecure-Requests':'1',
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                 }
        self.url_movie = '占位符'
        self.haoma = '占位符'
        self.movie_name = '占位符'


    def score(self, x):
        if x == ['allstar10', 'rating'] or x == ['ll', 'bigstar', 'bigstar10']:
            stars = '★☆☆☆☆'
        elif x == ['allstar20', 'rating'] or x == ['ll', 'bigstar', 'bigstar20']:
            stars = '★★☆☆☆'
        elif x == ['allstar30', 'rating'] or x == ['ll', 'bigstar', 'bigstar30']:
            stars = '★★★☆☆'
        elif x == ['allstar40', 'rating'] or x == ['ll', 'bigstar', 'bigstar40']:
            stars = '★★★★☆'
        elif x == ['allstar50', 'rating'] or x == ['ll', 'bigstar', 'bigstar50']:
            stars = '★★★★★'
        elif x == ['ll', 'bigstar', 'bigstar05']:
            stars = '☆☆☆☆☆'
        elif x == ['ll', 'bigstar', 'bigstar15']:
            stars = '★☆☆☆☆'
        elif x == ['ll', 'bigstar', 'bigstar25']:
            stars = '★★☆☆☆'
        elif x == ['ll', 'bigstar', 'bigstar35']:
            stars = '★★★☆☆'
        elif x == ['ll', 'bigstar', 'bigstar45']:
            stars = '★★★★☆'
        else:
            stars = '☆☆☆☆☆'
        return stars


    def search(self, name):
        url_search = 'http://api.douban.com/v2/movie/search?q=' + name
        r = requests.get(url_search, headers=self.h, timeout=7)
        r = r.json()
        self.haoma = r['subjects'][0]['id']
        self.url_movie = r['subjects'][0]['alt']


    def info(self,name):
        self.search(name)
        r = requests.get(self.url_movie, headers=self.h2, timeout=7)    
        bs = BeautifulSoup(r.text, 'lxml')
        self.movie_name = bs.find('h1').text.replace('\n',' ').replace(' ','')
        print(self.movie_name)    
        scores = bs.find('strong', class_="ll rating_num").text
        stars = bs.find('div', class_=re.compile("ll bigstar bigstar.*")).get('class')
        print('\n'+self.score(stars),'豆瓣评分 : ' + scores)
        print(bs.find('div', id='info').text)   
        print(bs.find('span', property="v:summary").text.replace(' ',''))


    def pinglun(self, num):
        n = (num-1)*10
        url='https://movie.douban.com/subject/'+self.haoma+'/comments?start='+str(n)+'&limit=20&sort=time&status=P&percent_type='
        r = requests.get(url, headers=self.h2, timeout=7)
        bs=BeautifulSoup(r.text, 'lxml')
        print('\n' + self.movie_name + '  短评:\n')
        for i in bs.find_all('div', class_="comment-item"):
            id_ = i.find('a').get('title')
            time_ = i.find('span', class_="comment-time ").get('title')
            try:
                x = i.find('span', class_=re.compile("allstar.* rating")).get('class')
                stars = self.score(x)
            except AttributeError:                
                stars = self.score('占位符')
            t = i.find('p', class_='').text
            print(id_)
            print(stars)
            print('发布于:',time_)
            print(t[1:]+'\n')

if __name__ == '__main__':
    d = Douban()  
    d.info('茉莉牌局')
    d.pinglun(1)


