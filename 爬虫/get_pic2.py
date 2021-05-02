#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

from bs4 import BeautifulSoup
import requests
import chardet
from fake_useragent import UserAgent
import re
import os

class get_pexels_pic(object):
    def __init__(self):
        self.headers={"User-Agent":UserAgent().chrome}
        self.base_url=r"https://www.jpxgmn.com"
        base_dir=os.path.dirname(os.path.abspath(__file__))
        self.pic_path=base_dir+"\img1"
        self.pic_num=1
        self.xilie_url=list()
        self.every_xilie_list=list()

    def jiexi_function(self,url):
        url = requests.get(url).content
        char_type = chardet.detect(url)
        url = url.decode(char_type["encoding"])
        soup = BeautifulSoup(url, "html.parser")
        return soup

    def get_all_xilie_url(self):
        #获取网站所有系列地址
        soup = self.jiexi_function(self.base_url)
        a=soup.select("div[class='sitenav']>ul>li>a")
        #第一个系列是首页，去掉
        for i in a[1:]:
            i=self.base_url+i["href"]
            self.xilie_url.append(i)
        for x in self.xilie_url:
            #获取每个系列下所有集合的链接
            self.get_every_xilie_urls(x)
    def get_every_xilie_urls(self,url):
        soup=self.jiexi_function(url)
        a=soup.select("li[class='related_box']>a")
        for y in a:
            y=self.base_url+y["href"]
            self.every_xilie_list.append(y)
        for abc in self.every_xilie_list:
            self.get_pic_url(abc)

    #获取所有图片链接
    def get_pic_url(self,url):
        # url=requests.get(url).content
        # char_type=chardet.detect(url)
        # url=url.decode(char_type["encoding"])
        soup=self.jiexi_function(url)
        #div_url=soup.find_all("div",class_="pagination")
        a=soup.select("div[class='pagination']>ul>a")
        print("该系列共有"+str(len(a))+"张图片:")
        for every_page in a:
            #拼接每页具体链接
            every_page=self.base_url+every_page["href"]
            #获取每个页面下具体图片链接
            self.get_page_pic(every_page)
    def get_page_pic(self,url):
        soup = self.jiexi_function(url)
        a=soup.select("article[class='article-content']>p>img")
        #获取每页图片的链接
        for page_pic in a:
            page_pic=self.base_url+page_pic["src"]
            #调用图片下载的函数
            self.down_pic(page_pic)
            self.pic_num+=1
    def down_pic(self,url):
        if not os.path.exists(self.pic_path):
            os.makedirs(self.pic_path)
        url=requests.get(url).content
        print("正在下在第"+str(self.pic_num)+"张图片...")
        with open(self.pic_path+"\\"+str(self.pic_num)+".jpg","wb")as file:
            file.write(url)

if __name__ =="__main__":
    url=r"https://www.jpxgmn.com/YouMi/17716.html"
    get_pic=get_pexels_pic()
    #get_pic.get_pic_url(url)
    get_pic.get_all_xilie_url()