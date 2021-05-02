#!/usr/bin/env python
#__*__ coding:utf-8 __*__

import logging.handlers
from time import strftime
import os

class Logger(logging.Logger):
    def __init__(self):
        super(Logger,self).__init__(self)
        log_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_name=os.path.join(log_dir,strftime("%Y%m%d")+".log")
        fh=logging.handlers.TimedRotatingFileHandler(log_name,"D",1,30,encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        sh=logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        formatter=logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(message)s]")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.addHandler(sh)
        self.addHandler(fh)
        sh.close()
        fh.close()