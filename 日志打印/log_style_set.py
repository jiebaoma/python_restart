#!/usr/bin/env python
#__*__ coding:utf-8 __*__
#author:yjzhai

import logging.handlers
from time import strftime
import os

class Logger(logging.Logger):
    def __init__(self):
        super(Logger,self).__init__(self)
        log_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_name=os.path.join(log_dir,strftime("%Y%m%d")+".log")
        #创建handler写入日志：每天生成一个日志，保留30天
        fh=logging.handlers.TimedRotatingFileHandler(self.log_name,"D",1,30,encoding="utf-8")
        #fh.suffix="%Y%m%d-%H%S"
        #设置日志级别
        fh.setLevel(logging.DEBUG)
        #创建控制台日志handler
        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        #设置日志样式
        formatter=logging.Formatter("[%(asctime)s]-[%(filename)s] -[line:%(lineno)d] --[%(levelname)s]:%(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.addHandler(fh)
        self.addHandler(sh)
        sh.close()
        fh.close()
