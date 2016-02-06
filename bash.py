#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import urllib
import json
from urllib import quote
import socket 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#设置超时
socket.setdefaulttimeout(10)
counter=1
# 获取图片url内容等 
def getImagesURL(max_number, word='美女'):
    search = quote(word)
    pn = 480
    while pn <= max_number:
        global counter
        url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
        page = urllib.urlopen(url)
        data = page.read()
        data = json.loads(data)
        saveImage(data, word)
        pn += 60
        
# 保存图片        
def saveImage(json, word):  
    global counter
    if not os.path.exists("./" + word):
        os.mkdir("./" + word)
    #判断名字是否重复
    index=len(os.listdir('./'+word))
    if os.path.exists("./"+word+"/"+str(counter)+".jpeg"):
            counter=index
    check='<html><body><h1>403 Forbidden</h1>'
    for info in json['imgs']:
        urllib.urlretrieve(info['objURL'], './' + word + '/' + str(counter) +'.jpeg')
        #判断防爬虫 <html><body><h1>403 Forbidden</h1>
        fp=open("./"+word+"/"+str(counter)+".jpeg")
        if not cmp(fp.readline(),'<html><body><h1>403 Forbidden</h1>\n'):
            os.remove("./"+word+"/"+str(counter)+".jpeg")
            counter-=1
        fp.close()
        counter += 1
        print "小黄图+1，已经保存"+str(counter-1)+"张小黄图\n"
    return counter

#获取后缀名
def getFix(name):
    return name[name.find('.'):]
#获取前缀
def getPrefix(name):
    return name[:name.find('.')]


#print getFix('123.txt')
#getImagesURL(390,'美女')
#getImagesURL(240,'二次元')
getImagesURL(1000,'帅哥')

