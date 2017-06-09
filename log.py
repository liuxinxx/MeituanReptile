#coding:utf-8 
import requests
from bs4 import BeautifulSoup
import os
import re
import json
import time
import datetime
from Main import *
class LOG(object):
    
    def printf_logFile(self,str):##写入日志文件
        FILE_ROOT = CurrentPath = os.getcwd()##获取当先脚本的运行目录
        Log_FileName =FILE_ROOT+'\\sz_shopinfo_test.log'
        str = log.LOG.whatstime()+str+'\r\n'
        log.LOG.write(str, Log_FileName, 1)    
    def whatsday(self):#获取时间，例如：2017_Apr_28_09_59_46.jpg,用来当做图片的name
        #  时间格式
        fmt = "%Y_%m_%d_%H_%M_%S"
        timestr = time.strftime(fmt,time.localtime())
        return str(datetime.datetime.now()).replace('.', '').replace(' ', '').replace('-', '').replace(':', '')
    def whatstime(self): 
        #  时间格式'%Y-%m-%d',time.localtime(time.time())('%Y-%m-%d %H:%M:%S'
        fmt = "[%Y-%m-%d  %H:%M:%S]: "
        timestr = time.strftime(fmt,time.localtime())
        return str(datetime.datetime.now()).replace('.', '').replace(' ', '').replace('-', '').replace(':', '')