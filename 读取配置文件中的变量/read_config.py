#!/usr/bin/env python
#__*__coding:utf-8__*__
#author:yjzhai

import os
import configparser

#获取当前文件父级目录地址
parent_dir=os.path.dirname(os.path.abspath(__file__))
#拼接配置文件所在路径
config_body=os.path.join(parent_dir,"config.ini")
#实例化并且读取配置文件内容
conf=configparser.ConfigParser()
conf.read(config_body)

#设置字典以存放配置文件中的变量
config_body_dict=dict()
config_body_dict["service_ip"]=conf.get("mysql_service","service_ip")
config_body_dict["port"]=conf.get("mysql_service","port")
config_body_dict["username"]=conf.get("mysql_service","username")
config_body_dict["password"]=conf.get("mysql_service","password")

for key,value in config_body_dict.items():
    print(key+":"+value)