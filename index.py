#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import urllib
import json
import socket
import urllib.request
import urllib.parse
import urllib.error
# 设置超时
import time

timeout = 5
socket.setdefaulttimeout(timeout)

counter = 1


class Crawler:
    # 睡眠时长
    __time_sleep = 0.1
    __amount = 0

    # 获取图片url内容等
    # t 下载图片时间间隔
    def __init__(self, t=0.1):
        self.time_sleep = t

    # 开始获取
    def __getImages(self, word='美女'):
        search = urllib.parse.quote(word)
        # pn int 图片数
        pn = 0
        while pn < self.amount:
            global counter
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                    pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            # 设置header防ban
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=headers)
                page = urllib.request.urlopen(req)
                data = page.read().decode('utf8')
            except UnicodeDecodeError as e:
                print('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                print("-----urlErrorurl:", url)
            except socket.timeout as e:
                print("-----socket timout:", url)
            else:
                # 解析json
                json_data = json.loads(data)
                self.__saveImage(json_data, word)
                # 读取下一页
                print("下载下一页")
                pn += 60
            finally:
                page.close()
        print("下载任务结束")
        return

    # 保存图片
    def __saveImage(self, json, word):
        global counter
        if not os.path.exists("./" + word):
            os.mkdir("./" + word)
        # 判断名字是否重复，获取图片长度
        counter = len(os.listdir('./' + word)) + 1
        for info in json['imgs']:
            try:
                if self.__downloadImage(info, word) == False:
                    counter -= 1
            except urllib.error.HTTPError as urllib_err:
                print(urllib_err)
                pass
            except:
                time.sleep(1)
                print("产生未知错误，放弃保存")
                continue
            else:
                print("小黄图+1,已有" + str(counter) + "张小黄图")
                counter += 1
        return

    # 下载图片
    def __downloadImage(self, info, word):
        global counter
        time.sleep(self.time_sleep)
        fix = self.__getFix(info['objURL'])
        urllib.request.urlretrieve(info['objURL'], './' + word + '/' + str(counter) + str(fix))

    # 获取后缀名
    def __getFix(self, name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    # 获取前缀
    def __getPrefix(self, name):
        return name[:name.find('.')]

    # page_number 页数 数量为 页数x60
    def start(self, word, page_number):
        self.amount = page_number * 60
        self.__getImages(word)


crawler = Crawler(0.05)
crawler.start('美女', 1)
#crawler.start('二次元 性感', 2)
#crawler.start('帅哥', 5)
