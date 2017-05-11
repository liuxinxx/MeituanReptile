#coding:utf-8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import HTMLParser
import requests
import random
import sys
import os
import subprocess
from urllib import urlencode
from urllib import quote
import csv
import codecs
def rad_ua():#获取随机的浏览器UA标识
    ua_list = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
            ]    
    ua = random.choice(ua_list)
    return ua

     
    ##利用PhantomJS来加载动态网页
def downloader_html(url,up_num):##利用PhantomJS获取网页数据
    '''
    url        :要下载的页面url
    up_num     :下拉的次数
    '''
    #print driver.service
    print '开始下拉页面加载!    URL为',url,'    下拉次数为:',up_num
    printf_logFile('浏览器打开完成，开始下拉页面加载！')
    jie_name = str(up_num)+'javacode.png'
    driver.get(url)    
    time.sleep(2)
    ##下拉浏览器页面使，页面完全加载 
    dian = ''
    print '网页下拉中',     
    for i in range(up_num): 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        ##进程休眠一秒等待网页加载完成    
        time.sleep(2) 
        dian =dian +'.'
        print '.', 
    printf_logFile('网页下拉中'+dian)
#     print '开始截图'
#     driver.get_screenshot_as_file(jie_name)##截图
#     print '截图完成',jie_name
    print driver.current_url, '页面获取完成，开始解析页面'
    printf_logFile('页面获取完成，开始解析页面')
    data = driver.page_source.encode("utf-8")
    # 解决页面转义
    html_parser = HTMLParser.HTMLParser()
    data = html_parser.unescape(data)   
    return data

def shopurl(data):##利用正则匹配链接，
    i = 0
    imgurl_list=['']
    mig = 0
    for m in re.findall(r'<img class="J-webp" src="(.*?.jpg).*?".*?>', data):
        imgurl_list.append(m)
        mig = mig +1
        print m
    print '图片链接结束' +str(mig)
    for v in re.findall(r'<a class="link f3 J-mtad-link".*?</a>', data):
        i=i+1
        print v        
        vv = re.match(r'<a.*?href="(.*?)".*?>(.*?)<',v)        
        print vv.group(1),' ',vv.group(2)
        print '结束' +str(i)
   
    for k in re.findall(r'&.*?class="link f3 J-mtad-link".*?&lt;/a&gt;', data):
        i=i+1
        print k
        kk = re.match(r'&.*?href="(.*?)".*?;(.*?)&',k)
        print kk.group(1),' ',kk.group(2)
        print '结束' +str(i)
def next_url(data):
    soup = BeautifulSoup(data,"html.parser")
    try:
        next_page = 'http://sz.meituan.com'+soup.find('a',attrs={'gaevent':'content/page/next'}).get('href')
        #print soup.find('a',attrs={'gaevent':'content/page/next'})
        return next_page
    except:        
        return '0'
def shopurl2(data,fenlei,city):##获取内容
    i=0#记录总数据条数
    j=0#记录爬取失败的数据条数
    soup = BeautifulSoup(data,"html.parser")
    print '网页:',len(data)
    printf_logFile('网页:'+str(len(data)))
    #next_page = 'http://sz.meituan.com'+soup.find('a',attrs={'gaevent':'content/page/next'}).get('href')
    #print '下一页为：',next_page
    
    
    #判断商家类型
    shop_flag =0#shop_flag =0 代表最普通 shop_flag = 1代表周边游 shop_flag = 2 代表酒店客栈 
    list_shop =soup.find_all('div',attrs={'data-mtd-showlog':'','data-mtd-clicklog':'','class':'poi-tile-nodeal'})#最普通
    if len(list_shop) == 0:
        list_shop = soup.find_all('div',class_='deal-tile')#周边游
        if len(list_shop) == 0:
            list_shop = soup.find_all('div',class_='hotel--main')#周边游
            if len(list_shop) == 0:
                print '解析输错！'
            else:
                shop_flag =2
        else:
            shop_flag = 1
    print 'shop_flag:',shop_flag
    for k in list_shop:
        shopinfo_scvlist=[]
        shopdata=[]
        i+=1
        #poi-tile__head J-mtad-link
        if shop_flag ==0:#普通
            print 'shop_flag =',shop_flag
            shop_url = k.find('a',class_='poi-tile__head J-mtad-link').get('href')
            shop_name = k.find('a',class_='link f3 J-mtad-link').get_text()
            shop_imgurl = k.find('img').get('src')
            try:
            #获取人均价格
                shop_jiage = k.find('span',class_='price').get_text()
                shop_jiage = shop_jiage[1:len(shop_jiage)]
            except:
                shop_jiage = k.find('span',class_='value').get_text()
                shop_jiage = shop_jiage[1:len(shop_jiage)]
            if shop_imgurl.find('http') == -1:
                shop_imgurl = k.find('img').get('data-src')
        if shop_flag ==1:#周边游
            print 'shop_flag =',shop_flag
            shop_url = k.find('a',class_='w-link J-mtad-link').get('href')
            shop_name = k.find('span',class_='xtitle').get_text()
            shop_imgurl = k.find('img').get('src')
            shop_jiage = k.find('p',class_='deal-tile__detail').get_text().replace(' ','').replace("\n","")
            print shop_jiage
            shop_jiage =shop_jiage[shop_jiage.rfind('¥')+1:len(shop_jiage)]
            if shop_imgurl.find('http') == -1:
                shop_imgurl = k.find('img').get('data-src')
                
        if shop_flag ==2:#酒店客栈
            print 'shop_flag =',shop_flag
            shop_url = k.find('a',class_='title').get('href')
            shop_name = k.find('a',class_='title').get_text()
            shop_imgurl = k.find('img').get('src')
            shop_jiage = '000'
            
            #shop_jiage =shop_jiage[shop_jiage.rfind('¥')+1:len(shop_jiage)]
            if shop_imgurl.find('http') == -1:
                shop_imgurl = k.find('img').get('data-src')
                
        try:
            op = '------------------------------------------------------------------------'+'\n\n'
            printf_logFile(op)
            print '商店图片链接: ',shop_imgurl
            printf_logFile('商店图片链接: '+shop_imgurl)
            
            print '店铺地址: ',shop_url
            printf_logFile('店铺地址: '+shop_url)
            
            print '店铺名称: ',shop_name
            printf_logFile('店铺名称: '+shop_name)
            
            print '价格:',shop_jiage
            printf_logFile('价格: '+shop_jiage)
            try:
                if(ping()==False):
                    print "等待网络重连！"
                    while(True):
                        print'.',
                        if(ping()==True):
                            break 
                        time.sleep(1)                       
                    print "网络连接成功！我们继续搞事情！"
                    time.sleep(2)
                    if shop_flag ==0:
                        list_shopinfo = jiexi(shop_url,shop_flag)
                    if shop_flag  ==1:#周边游
                        list_shopinfo = jiexi_zby(shop_url,shop_flag)
                    if shop_flag  ==2:#周边游
                        list_shopinfo = jiexi_hotel(shop_url,shop_flag)
                    for g in range(len(list_shopinfo)):
                        print str(list_shopinfo[g][0]),':',str(list_shopinfo[g][1])
                    #shopinfo_scvlist.append(object)
                else:
                    if shop_flag ==0:
                        list_shopinfo = jiexi(shop_url,shop_flag)
                    if shop_flag  ==1:#周边游
                        list_shopinfo = jiexi_zby(shop_url,shop_flag)
                    if shop_flag  ==2:#周边游
                        list_shopinfo = jiexi_hotel(shop_url,shop_flag)
                    '''
                    [['地区',area],['店铺名',' '],['地址',shop_address],['联系电话',shop_number[3].get_text()],['分类',sort]]
                    0    地区
                    1    店铺名
                    2    店铺地址
                    3    联系电话
                    ''' 
                    for g in range(len(list_shopinfo)):
                        print str(list_shopinfo[g][0]),':',str(list_shopinfo[g][1])
                print 
                print op
            except Exception,e:
                print Exception,':',e
                print "解析商铺详情时，发生意外稍等....."
                time.sleep(2)
                if shop_flag ==0:
                    list_shopinfo = jiexi(shop_url,shop_flag)
                if shop_flag ==1:#周边游
                    list_shopinfo = jiexi_zby(shop_url,shop_flag)
                if shop_flag ==2:#周边游
                    list_shopinfo = jiexi_hotel(shop_url,shop_flag)
            printf_logFile('开始将数据写入CSV文件')   
            print '开始将数据写入CSV文件'
            try:
                #['城市','地区','店铺分类','店铺名称','地址','店铺url','电话','人均','店铺具体分类','商家店招图片url','图片本地名字']
                #fenlei
                '''
                1    地区
                2    店铺名
                3    店铺地址
                4    联系电话
                5    详细分类
                '''
                shopdata.append(city)#店铺所在城市
                shopdata.append(list_shopinfo[0][1])#店铺地区
                shopdata.append(fenlei)#分类
                shopdata.append(list_shopinfo[1][1])#店铺名字
                shopdata.append(list_shopinfo[2][1])#店铺地址
                shopdata.append(shop_url)#店铺url
                shopdata.append(list_shopinfo[3][1])#联系方式
                shopdata.append(shop_jiage)#人均
                shopdata.append(list_shopinfo[4][1])#店铺具体分类
                shopdata.append(shop_imgurl)#商家店招图片url
                ##获取图片格式
                if shop_imgurl.find('jpg') != -1:
                    img_name = whatsday()+'.jpg'
                elif shop_imgurl.find('png') != -1:
                    img_name = whatsday()+'.png'
                elif shop_imgurl.find('jpeg') != -1:
                    img_name = whatsday()+'.jpeg'
                #img_name = whatsday()+'.jpg'
                shopdata.append(img_name)#图片本地名字
                
                shopinfo_scvlist.append(shopdata)
                dow_img(shop_imgurl,img_name)
               
                ##将商铺信息写入csv文件
                writer_csv.writerows(shopinfo_scvlist)
                #svae_csv(shopinfo_scvlist,writer)
                print '写入数据成功！'
                printf_logFile('写入数据成功！' )
            except Exception,e: 
                print '写入数据失败！',Exception,':' ,e
                printf_logFile('写入数据失败！'+str(Exception)+':' +str(e))
            print op      
        except Exception,e: 
            j+=1
            print '发生异常：',Exception,':' ,e
            printf_logFile('发生异常:'+str(Exception)+':' +str(e))
            time.sleep(3)
            print "这个爬不动",k
            printf_logFile("这个爬不动"+shop_url)
            print k.find('img')
            
        #店铺名称、地址、店铺url、电话、人均、店铺分类、商家店招图片url
        #head =['店铺名称','地址','店铺url','电话','人均','店铺分类','商家店招图片url']
    printf_logFile("总共"+str(i)+"条！  "+str(j)+'条,爬不动！')
    print "总共",str(i),"条！  ",str(j),'条,爬不动！'

#获取地区分类
def svae_csv(csvdata,writer):
    '''
    csvfile_name :需要保存的文件名
    csvdata      :要保存的数据
    csvhead      :csv文档头
    '''
#   writer.writerow(csvhead)
#     data = [
#       ['1','http://www.xiaoheiseo.com/','小黑'],
#       ['2','http://www.baidu.com/', '百度'],
#       ['3','http://www.jd.com/', '京东']
#     ]
    writer.writerows(csvdata)
    #关闭CSV文件
def fenlei(soup):##获取全国各个地区链接
    list_fenlei = []    
    div_list = soup.find_all("div",class_="J-nav-item")
    for v in div_list:
        for k in v.find_all('li'):
            list =[]
            k = k.find('a')        
            fenlei_url =k.get('href')
            fenlei_name =k.get_text()
            list.append(fenlei_name)
            list.append(fenlei_url)
            list_fenlei.append(list)           
    return list_fenlei

def write(str,file_name,flag):#将制定的字符串写入指定的文件中，当标记flag为1时，代表追加写入，为2时代表清除源文件后写入
    if flag == 1:
        file_object = open(file_name, 'a')
        file_object.write(str)
        file_object.close()
    if flag ==2:
        file_object = open(file_name, 'wb')
        file_object.write(str)
        file_object.close()
def jiexi_zby(url,shop_flag):##获取周边游店铺详情
    while True:
        try:
            driver.get(url)
            break
        except Exception,e:
            print 'url:',url 
            printf_logFile('url:'+url ) 
            print Exception,":",e
            printf_logFile('error'+Exception+":"+e)
            print '页面打开错误，重新打开中..'
    print '页面加载完成！'
    printf_logFile('页面加载完成！')
    dian =''
    for i in range(2): 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        ##进程休眠一秒等待网页加载完成    
        time.sleep(2) 
        dian =dian +'.'
        print '.',    
    data = driver.page_source
    # 解决页面转义
    html_parser = HTMLParser.HTMLParser()
    data = html_parser.unescape(data)
    soup = BeautifulSoup(data,"html.parser")  
    ##获取商品分类信息
    print '周边游类'
    printf_logFile('周边游类')
    sort1 = soup.find('a',attrs={'gaevent':'crumb/index'}).get_text()
    sort2 = soup.find('a',attrs={'gaevent':'crumb/category/1'}).get_text()
    sort3 = soup.find('a',attrs={'gaevent':'crumb/category/2'}).get_text()
    sort = sort1+'\\'+sort2+'\\'+sort3
    data1 = soup.find_all('div',class_="biz-info__content")
    i = 0
    for g in data1:
        s = g
        i= i+1
    print str(i)
    if i!=0:       
        #取店铺名字
        shop_name = soup.find('a',attrs={'class':'poi-link'}).get('title')     
        ##获取店铺地址
        shop_address = s.find('div',class_="biz-item field-group").get('title')
        
        #获取联系方式
        shop_number = s.find_all('div',class_="biz-item")
        number =''
        for g in range(len(shop_number)):
            if shop_number[g].get_text().find('电话')!=-1:#没找到返回-1
                number=shop_number[g].get_text()
                number = number[number.find('：')+1:len(number)]
                number.replace(' ', '')
                break           
        #获取地区信息       
        area = soup.find('span',attrs={'class':'deal-component-title-prefix'}).get_text()
        area = area[1:len(area)-1]#地区信息
       
        list_shopinfo = [['地区',area],['店铺名',shop_name],['地址',shop_address],['联系电话',number],['分类',sort]]
        print "地址：",shop_address,'店铺名字：',shop_name,"    联系电话：",number,'分类:'+sort1+'\\'+sort2+'\\'+sort3
        printf_logFile("地址："+shop_address+"    联系电话："+number+'分类:'+sort1+'\\'+sort2+'\\'+sort3)
        return list_shopinfo            
    else:
        print "网页爬取出错"
        return 'error'  
def jiexi_hotel(url,shop_flag):##获取周边游店铺详情
    while True:
        try:
            driver.get(url)
            break
        except Exception,e:
            print 'url:',url 
            printf_logFile('url:'+url ) 
            print Exception,":",e
            printf_logFile('error'+Exception+":"+e)
            print '页面打开错误，重新打开中..'
    print '页面加载完成！'
    printf_logFile('页面加载完成！')
    dian =''
    for i in range(2): 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        ##进程休眠一秒等待网页加载完成    
        time.sleep(2) 
        dian =dian +'.'
        print '.',    
    data = driver.page_source
    # 解决页面转义
    html_parser = HTMLParser.HTMLParser()
    data = html_parser.unescape(data)
    soup = BeautifulSoup(data,"html.parser")  
    ##获取商品分类信息
    print '酒店客栈'
    printf_logFile('酒店客栈')
    sort = soup.find('div',attrs={'class':'bread-nav'}).get_text().replace(' ','').replace('»', '\\').replace('\n', '')
    
    
    try:   
        #获取地区信息       
        area = soup.find('a',attrs={'gaevent':'crumb/area/1'}).get_text()
        #取店铺名字
        shop_name = soup.find('h5',attrs={'class':'uix-tooltip'}).get('title')     
        ##获取店铺地址
        shop_address = soup.find('span',class_="title").get('title')
        
        #获取联系方式 soup.find('dd',attrs={'class':'col-d-9 col-l-12 col-m-9 col-last'}).get_text()
        number = soup.find('dd',attrs={'class':'col-d-9 col-l-12 col-m-9 col-last'}).get_text().replace(' ','').replace('\n','')
        
        list_shopinfo = [['地区',area],['店铺名',shop_name],['地址',shop_address],['联系电话',number],['分类',sort]]
        
        print "地址：",shop_address,'店铺名字：',shop_name,"    联系电话：",number,'分类:',sort
        
        printf_logFile("地址："+shop_address+"    联系电话："+number+'分类:'+sort)
        
        return list_shopinfo            
    except Exception,e:
        print "网页爬取出错",Exception,':',e
        return 'error' 
def jiexi(url,shop_flag):##获取店铺详情
    # 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H52908D8264XMC5D"
    proxyPass = "A31BCBE58954E8B1"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    UA = rad_ua() ##从ua_list中随机取出一个字符串
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）
    #data = requests.get(url, headers=headers,proxies=proxies)
    data = requests.get(url, headers=headers) ##这样服务器就会以为我们是真的浏览器了
    print data.status_code
    if data.status_code == 402:
        os._exit(0)
    #防止ping检测过了，但是刚好网断了，造成利用本地IP访问，@~~~我的本地IP是被封的。。。。
    if data.status_code!=200:
        print '出现异常开始等待',
        printf_logFile('出现异常开始等待')
        while(True):            
            UA = rad_ua() ##从self.user_agent_list中随机取出一个字符串（聪明的小哥儿一定发现了这是完整的User-Agent中：后面的一半段）
            headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）        
            data = requests.get(url, headers=headers,proxies=proxies) ##这样服务器就会以为我们是真的浏览器了
            #data = requests.get(url,)
            print '.',
            
            if data.status_code==200:
                print 
                printf_logFile('异常结束！继续搞事情')
                print '异常结束！继续搞事情'
                break
            time.sleep(2)
    else:
        print '网页请求成功！','返回代码:',data.status_code
        printf_logFile('网页请求成功！'+'返回代码:'+str(data.status_code))
    soup = BeautifulSoup(data.text,"html.parser")    
    if shop_flag == 0:        
        ##获取商品分类信息
        sort1 = soup.find('a',attrs={'gaevent':'crumb/index'}).get_text()
        sort2 = soup.find('a',attrs={'gaevent':'crumb/category/1'}).get_text()
        sort3 = soup.find('a',attrs={'gaevent':'crumb/category/2'}).get_text()
        sort = sort1+'\\'+sort2+'\\'+sort3
        area = soup.find('a',attrs={'gaevent':'crumb/area/1'}).get_text()#地区信息
        
        data = soup.find_all('div',class_="fs-section__left")
        i = 0
        for g in data:
            s = g
            i= i+1
        #print str(i)
        if i!=0:
            #获取店铺名字
            shop_name = s.find('span',class_="title").get_text()
            
            ##获取店铺地
            shop_address = s.find('span',class_="geo").get_text()
            
            #获取联系方式
            shop_number = s.find_all('p',class_="under-title")  
            #csvhead = ['城市','地区','店铺分类','店铺名称','地址','店铺url','电话','人均','店铺具体分类','商家店招图片url','图片本地名字'] 
            list_shopinfo = [['地区',area],['店铺名',shop_name],['地址',shop_address],['联系电话',shop_number[1].get_text()],['分类',sort]]     
            #list_shopinfo = [['店铺名',shop_name],['地址',shop_address],['联系电话',shop_number[1].get_text()],['分类',sort]]
            printf_logFile("地区"+area+"   地址："+shop_address+"    联系电话："+shop_number[1].get_text()+'分类:'+sort1+'\\'+sort2+'\\'+sort3)
            return list_shopinfo
        else:
            print "网页爬取出错"
            return 'error'
def printf_logFile(str):##写入日志文件
    Log_FileName ='K:\\javacode\\weibo\\test\\data\\sz_shopinfo_test.log'
    str = whatstime()+str+'\r\n'
    write(str, Log_FileName, 1)    
def whatsday():#获取时间，例如：2017_Apr_28_09_59_46.jpg,用来当做图片的name
    #  时间格式
    fmt = "%Y_%m_%d_%H_%M_%S"
    timestr = time.strftime(fmt,time.localtime())
    return timestr
def whatstime(): 
    #  时间格式'%Y-%m-%d',time.localtime(time.time())('%Y-%m-%d %H:%M:%S'
    fmt = "[%Y-%m-%d  %H:%M:%S]: "
    timestr = time.strftime(fmt,time.localtime())
    return timestr

def dow_img(img_url,img_name):#下载指定链接的图片
    headers ={'User-Agent': rad_ua()}
    img = requests.get(img_url,headers=headers)

    f = open('K:\\javacode\\weibo\\test\\data\\sz_shopimage\\'+img_name,'ab')
    f.write(img.content)
    f.close()

def ping():#判断网络是否联通
    UA = rad_ua() ##从ua_list中随机取出一个字符串
    headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）
    data = requests.get('http://sz.meituan.com', headers=headers) ##这样服务器就会以为我们是真的浏览器了
    if data.status_code ==200:
        return True
    else:
        return False  
def getCity():##返回城市二维列表[0]url [1]城市名字
    cityUrl_list=[]
    for line in open("city.txt"):
        list_t =[]  
        line=line.replace("\n","")
        lines=line.split("^") 
        list_t.append(lines[0])
        list_t.append(lines[1])
        cityUrl_list.append(list)
    return cityUrl_list
#获取城市列表
# listCity = getCity()
# for g in range(len(listCity)):
#     print listCity[g][0],listCity[g][1]
##listCity[g][0]为城市s
if __name__ == '__main__':
    print '开始'
    printf_logFile('开始')
    sz = 'http://sz.meituan.com/'
    city ='深圳'
    print '创建csv文件'
    printf_logFile('创建csv文件')
    ##创建csv文件   
    try:        
        csvfile_name = 'K:\\javacode\\weibo\\test\\data\\sz_shop.csv'
        csvfile = file(csvfile_name,'ab+')
        csvfile.write(codecs.BOM_UTF8)
        writer_csv = csv.writer(csvfile)
        csvhead = ['城市','地区','店铺分类','店铺名称','地址','店铺url','电话','人均','店铺具体分类','商家店招图片url','图片本地名字']
        writer_csv.writerow(csvhead)
        print 'csv文件创建成功！'
        printf_logFile('csv文件创建成功！')
    except Exception,e:
        print '写入CSV文件错误',Exception,":",e
        printf_logFile('写入CSV文件错误'+Exception+":"+e)
    # 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H52908D8264XMC5D"
    proxyPass = "A31BCBE58954E8B1"

    service_args = [
        "--proxy-type=http",
        "--proxy=%(host)s:%(port)s" % {
            "host" : proxyHost,
            "port" : proxyPort,
        },
        "--proxy-auth=%(user)s:%(pass)s" % {
            "user" : proxyUser,
            "pass" : proxyPass,
        },
    ]
    phantomjs_path = r"phantomjs"
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    #伪造浏览器UA标识，防止网站反爬虫
    ua =rad_ua()##获取浏览器UA
    
    baidu_ua = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html）'
    dcap["phantomjs.page.settings.userAgent"] = (ua)
    #,executable_path=phantomjs_path,service_args=service_args
    driver = webdriver.PhantomJS(desired_capabilities=dcap,executable_path=phantomjs_path)
    # #代理IP
    # proxy=webdriver.Proxy()
    # proxy = Proxy(
    #     {
    #         'proxyType': ProxyType.MANUAL,
    #         'httpProxy': '114.231.153.12:20059'  # 代理ip和端口
    #     }
    # )
    # # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
    # proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
    # driver.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
    
    soup = BeautifulSoup(downloader_html(sz,1),'lxml')
#     url = 'http://hotel.meituan.com/shenzhen/c-jingjijiudian'
#     shopurl2(downloader_html(url,3),'酒店',city)
    listfenlei = fenlei(soup)
    print '获取商品列表成功！' ,len(listfenlei)
    printf_logFile('获取商品列表成功！'+str(len(listfenlei)))
    # #获取分类列表
    cai = 0
    for g in range(len(listfenlei)):
        if listfenlei[g][1].find('hotel')!=-1 and listfenlei[g][1].find('trip')==-1 and listfenlei[g][1].find('dianying')==-1 and g!=0:
            ##listfenlei[g][1] 每个城市的小分类
            url_txt = listfenlei[g][0].encode("utf8")#分类中文
            url = listfenlei[g][1].encode("utf8")#分类url
            url= quote(url,'://')#对URL进行转码，防止中文造成url的打开错误
#             if url_txt=='温泉':
#                 cai = 1
#             if cai == 1:
            print '开始爬取 ：',sz,'分类为：',url_txt,'链接为：',url
            printf_logFile('开始爬取 ：'+sz+'分类为：'+url_txt+'链接为：'+url)
            data = downloader_html(url,10) 
            next_page = next_url(data)    
            print '下一页为：',next_page
            printf_logFile('下一页为：'+next_page)         
            shopurl2(data,url_txt,city)
            while True: 
                if next_page=='0':
                    break
                data = downloader_html(next_page,10)
                shopurl2(data,url_txt,city) 
                next_page = next_url(data)   
                print '下一页为：',next_page
                printf_logFile('下一页为：'+next_page)
                  
#    shopurl2(downloader_html('http://sz.meituan.com/category/daijinquan_meishi'),'代金券')
    csvfile.close()  
    driver.quit()#关掉浏览器