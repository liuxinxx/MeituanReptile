#coding:utf-8 
import requests
from bs4 import BeautifulSoup
import os
import re
import json
import time
import datetime
class LOG(object):
    def write(self,str,file_name,flag):#将制定的字符串写入指定的文件中，当标记flag为1时，代表追加写入，为2时代表清除源文件后写入
        if flag == 1:
            file_object = open(file_name, 'a')
            file_object.write(str)
            file_object.close()
        if flag ==2:
            file_object = open(file_name, 'wb')
            file_object.write(str)
            file_object.close()
    def printf_logFile(self,str,file):##写入日志文件
        Log_FileName =file+'\\shopinfo_movie.log'
        str = self.whatstime()+str+'\r\n'
        self.write(str, Log_FileName, 1)    
    def whatsday(self):
        return str(datetime.datetime.now()).replace('.', '').replace(' ', '').replace('-', '').replace(':', '')
    def whatstime(self): 
        #  时间格式'%Y-%m-%d',time.localtime(time.time())('%Y-%m-%d %H:%M:%S'
        fmt = "[%Y-%m-%d  %H:%M:%S]: "
        timestr = time.strftime(fmt,time.localtime())
        return timestr