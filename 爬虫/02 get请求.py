#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

""""
get请求有中文时显示的是url编码，所以有中文时需要转成url编码格式，可通过wd字典解决
"""
from urllib import request
import urllib
from fake_useragent import UserAgent

url=r"http://www.baidu.com/s?"
heders={"User-Agnet":UserAgent().chrome}
wd={"wd":"北京"}
#构造url编码
wd=urllib.parse.urlencode(wd)
url=url+wd
req=request.Request(url,headers=heders)
response=request.urlopen(req).read().decode()
print(response)
