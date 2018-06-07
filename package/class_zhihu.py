# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import pandas as pd
import json
import tqdm
import time


class Zhihu:
    
    def __init__(self):
        self.h ={'Cookie':'q_c1=cdbc5287efc7411a96e1f04701e7204a|1506674624000|1506674624000; _zap=872910e0-4135-4373-92f8-a9d808fb45b7; d_c0="AJBCCxlfdwyPTiXMikg-z9khwBK8cHzcH7s=|1506949314"; _xsrf=c5c376b42f969b9f3abc447bcaf0cc79; q_c1=cdbc5287efc7411a96e1f04701e7204a|1514605432000|1506674624000; __utma=51854390.1628856114.1513919563.1514336822.1514817971.6; __utmz=51854390.1514817971.6.5.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/32004075; __utmv=51854390.000--|2=registration_date=20160509=1^3=entry_date=20170929=1; l_cap_id="NDUzNzQ3ODc5ZTZkNGQxYmFlMTYzOTQ5NmRlM2EzNDY=|1514820320|8847ec43c3c3b14356d522d88bd8f90fd5db571b"; r_cap_id="ZWRlOTNlODY1MTM5NDZjZWE1YTk5OGE5OWJlMTc1YmE=|1514820320|a0402e9d5286b8087506de25627eac0cca8a4f8a"; cap_id="YTQyYTU1ZWNhMTllNGU0MmI3ZGZkNjVmMWFiMjY5MTc=|1514820320|7f459547f11546f8a4d71b146f721dbac4d22384"; capsion_ticket="2|1:0|10:1514820322|14:capsion_ticket|44:MTMxNGNkMzE5YTNiNDRlZGEwY2NhN2QzMzBlMTMxNmQ=|05508f1050be0524a43d6adc2ad14daede8fc0afa7eccdedd9d3b1eb6d073c29"; z_c0="2|1:0|10:1514820324|4:z_c0|92:Mi4xVEg0QkF3QUFBQUFBa0VJTEdWOTNEQ1lBQUFCZ0FsVk41S0EzV3dBRy1RSkxGOFQ2RjZSbzh6c29JSVFHbko0aVhn|f1fb78b241c24195b880a09291d723e443c087ae0f3a2211a5ae5aa126091123"; aliyungf_tc=AQAAAK7lahG+PAAAMkhuJBMiUOucgAq8; _xsrf=c5c376b42f969b9f3abc447bcaf0cc79',
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Language':'zh-CN,zh;q=0.8',
#                 'Host':'www.zhihu.com',
                 'Referer':'https://www.zhihu.com/',
                 'Connection':'keep-alive',
                 'x-udid':'AJBCCxlfdwyPTiXMikg-z9khwBK8cHzcH7s='
                 }
        self.h2 ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Language':'zh-CN,zh;q=0.8',
                 'Cache-Control':'max-age=0',
                 'Connection':'keep-alive',
                 'Cookie':'_zap=157e4f4b-a7ba-485a-b5a3-3c9b250f84ca; d_c0="AIArQ-sdDw2PTgrrcjAU1ekfr2_zWE0nd8g=|1517132775"; __DAYU_PP=AqQz6JnUeZY2Mnu3ENQA7c50d7133647; q_c1=bea8f5ba2633429584afe1db593444d4|1521034963000|1515722149000; r_cap_id="M2I2OTI3MWM3ODljNGJhNGI2YzhlOWJlMjVlMTIxN2E=|1521791016|fb30fe79346e3562ac382d6152da8c77943bf4e1"; cap_id="Njc3YTYxNmRkZWNiNDA1Nzg3NzE2ZDQwN2ExMjI5YmI=|1521791016|06c769f3d943919bdce321ff904ef948f0756cb9"; XSRF-TOKEN=2|2438fc43|425ac976475dc5260959c4704015c871175dd17a16599a6e475e9a21160ecf27160ccf7a|1521791520; capsion_ticket="2|1:0|10:1521791553|14:capsion_ticket|44:NjM2NDI1NDZlOWMyNDA5NWE0ZjNlNGFjMWRlODUxN2M=|e639905674cd0a7be8d0957085880c38abd75859220c7f2befe37b379a9ded66"; z_c0=Mi4xVEg0QkF3QUFBQUFBZ0N0RDZ4MFBEUmNBQUFCaEFsVk5VZ0NpV3dBMW1BRFNfOFF5NVNBbkpvTkdWbTZ5RHpLUXVB|1521791570|bafa2746a1ecdefaaf81875bdd9b1dec6a0d8cf7; __utma=51854390.525112154.1521700951.1521770833.1521790219.3; __utmz=51854390.1521790219.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19723895/hot; __utmv=51854390.100--|2=registration_date=20160509=1^3=entry_date=20160509=1; _xsrf=d334b7a9-34ce-4784-8015-dc7a28730a77',
                 'Host':'zhuanlan.zhihu.com',
                 'If-None-Match':'W/"d4b2dcc5e53bfa6f3ae565ae9f03e50dd7d3f1f5"',
                 'Upgrade-Insecure-Requests':'1',
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
                 }
        self.zhihu_list = []
        self.zhihu_df = pd.DataFrame()


    def zhihu_mulu(self, keyword, num):
        zhihu_dic = {}
        d = {'q':keyword,
             'correction':'1',
             'type':'content',
             'offset':str(num*10)
             }
        url = 'https://www.zhihu.com/r/search?'+urlencode(d)
        r = requests.get(url, headers = self.h, timeout = 5)
        zhihu_json = r.json()
        zhihu_json = zhihu_json['htmls']
        for i in zhihu_json:
            bs = BeautifulSoup(i, 'lxml')
            self.zhihu_list.append(bs.find(class_="js-title-link").text)
            l = bs.find('a').attrs['href'][10:]
            zhihu_dic[bs.find(class_="js-title-link").text] = l
        zhihu_dic = pd.DataFrame.from_dict(zhihu_dic, orient = 'index')
        zhihu_dic = zhihu_dic.reset_index(drop = False)
        zhihu_dic.columns = ['题目', '链接']
        self.zhihu_df = self.zhihu_df.append(zhihu_dic)
        self.zhihu_df = self.zhihu_df.reset_index(drop = True)
        

    def zh_lists(self, keyword):
        self.zhihu_list = []
        self.zhihu_df = pd.DataFrame()
        try:
            for i in tqdm.tqdm(range(5),ncols=70): # ncols是设定进度条的显示长度
                self.zhihu_mulu(keyword, i)
        except ValueError:
            print('该问题仅有 '+str(i)+' 页')
        return self.zhihu_list


    def read_zhihu(self, x, num):
        data = {'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics',
                'offset':str((num-1)*20),
                'limit':'20',
                'sort_by':'default'
                }
        code = self.zhihu_df.iloc[list(self.zhihu_df['题目']).index(x),1]
        url = 'https://www.zhihu.com/api/v4/questions/'+code+'/answers?'+urlencode(data)
        r = requests.get(url, headers=self.h, timeout=5)
        try:
            zhihu_json = r.json()
            zhihu_json = zhihu_json['data']
            print(x+' -- 第'+str(num)+'页\n\n')
            for i in zhihu_json:
                t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['created_time']))
                print(i['author']['name'])
                print('发布于: '+t) 
                pinglun = i['content']
                pinglun = BeautifulSoup(pinglun, 'lxml')
                for j in pinglun.strings:
                    print(j)
                print('\n\n')
#                pinglun = re.sub(re.compile('(<.*?>)'), '', pinglun)
        except json.decoder.JSONDecodeError:
            print(x+' -- 是一个知乎专栏', '\n')
            url = 'https://zh'+code
            r = requests.get(url, headers=self.h, timeout=5)
            r.encoding = 'utf8'
            bs = BeautifulSoup(r.text,'lxml')
            b = bs.find('div',class_="RichText ztext Post-RichText")
            for i in b.strings:
                print(i)

