#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

import re
import requests
import chardet
from fake_useragent import UserAgent
import os

class get_pic(object):
    def __init__(self):
        self.header={"User-Agent":UserAgent().Chrome}
        self.base_url="https://www.taotuxp.com/252248.html/"
        self.url_list=[]
        self.pic_num=1
        self.pic_base_path=os.path.dirname(os.path.abspath(__file__))
    #获取首页一共多少个系列
    # def home_page_xilie_url(self):
    #     res = requests.get(self.base_url, headers=self.header).content
    #     char_type = chardet.detect(res)
    #     res = res.decode(char_type["encoding"])
    #     pat0 = re.compile('<h2><a href="(.*?)" rel="bookmark" target="_blank" title="')
    #     result = pat0.findall(res,re.S)
    #     return result

    #获取该系列下所有页面的url
    def get_xilie_url(self):
        #get_url=self.home_page_xilie_url()
        #for res in get_url:
            res = requests.get(self.base_url, headers=self.header).content
            char_type = chardet.detect(res)
            res = res.decode(char_type["encoding"])
            pat = re.compile('<a href="https://www.taotuxp.com(.*?).html/')
            result = pat.findall(res)
            end_page=len(result)+2
            for i in range(1,int(end_page)):
                self.url_list.append(self.base_url+str(i))
            return self.url_list
    #解析每页的具体内容
    def parse_url(self):
        pic_url=self.get_xilie_url()
        for i in pic_url:
            res=requests.get(i,headers=self.header).content
            char_type=chardet.detect(res)
            res=res.decode(char_type["encoding"])
            pat=re.compile('<p><img src="(.*?)" alt')
            pat1=re.compile('<h1>(.*?)</h1>')
            pic_url=pat.findall(res,re.S)
            pat1=pat1.findall(res)
            for i in pic_url:
                print("正在下载第"+str(self.pic_num)+"张图片")
                pic_dir = os.path.join(self.pic_base_path,pat1[0])
                if not os.path.exists(pic_dir):
                    os.mkdir(pic_dir)
                pic_name=pic_dir+"\\"+str(self.pic_num)+".jpg"
                pic=requests.get(i,timeout=10).content
                with open(pic_name,"wb") as f:
                    f.write(pic)
                self.pic_num+=1
if __name__ == "__main__":
    get_pic=get_pic()
    get_pic.parse_url()