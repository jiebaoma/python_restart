#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

""""
功能：爬取百度首页源代码
字符串在python内部表示的是Unicode编码
"""
from urllib import request
import re

url=r"http://www.baidu.com/"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
req=request.Request(url,headers=header)
#decode:将其他编码转成Unicode，encode:将Unicode编码转成其他编码
response=request.urlopen(req).read().decode()
pat=r"<title>(.*?)</title>"
data=re.findall(pat,response)
print(data[0])
print(data)