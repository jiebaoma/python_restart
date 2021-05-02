#!/usr/bin/env python
#__*__coding:utf-8 __*__

from urllib import request
import re
from fake_useragent import UserAgent
url=r"http://www.baidu.com"
header={"User-Agent": UserAgent().chrome}
req=request.Request(url=url,headers=header)
response=request.urlopen(req).read().decode()
pattern=r"<title>(.*?)</title>"
head=re.findall(pattern,response)
print(head[0])

