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


class Crawler:
    # 睡眠时长
    __time_sleep = 0.1
    __amount = 0
    __start_amount = 0
    __counter = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    __per_page = 30

    # 获取图片url内容等
    # t 下载图片时间间隔
    def __init__(self, t=0.1):
        self.time_sleep = t

    # 获取后缀名
    @staticmethod
    def get_suffix(name):
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    # 保存图片
    def save_image(self, rsp_data, word):
        if not os.path.exists("./" + word):
            os.mkdir("./" + word)
        # 判断名字是否重复，获取图片长度
        self.__counter = len(os.listdir('./' + word)) + 1
        for image_info in rsp_data['data']:
            try:
                if len(image_info['replaceUrl']) < 1:
                    continue
                obj_url = image_info['replaceUrl'][0]['ObjUrl']
                thumb_url = image_info['thumbURL']
                url = 'https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=%s&thumburl=%s' % (urllib.parse.quote(obj_url), urllib.parse.quote(thumb_url))
                time.sleep(self.time_sleep)
                suffix = self.get_suffix(obj_url)
                # 指定UA和referrer，减少403
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'),
                ]
                urllib.request.install_opener(opener)
                # 保存图片
                urllib.request.urlretrieve(url, './' + word + '/' + str(self.__counter) + str(suffix))
            except urllib.error.HTTPError as urllib_err:
                print(urllib_err)
                continue
            except Exception as err:
                time.sleep(1)
                print(err)
                print("产生未知错误，放弃保存")
                continue
            else:
                print("小黄图+1,已有" + str(self.__counter) + "张小黄图")
                self.__counter += 1
        return

    # 开始获取
    def get_images(self, word='美女'):
        search = urllib.parse.quote(word)
        # pn int 图片数
        pn = self.__start_amount
        while pn < self.__amount:

            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=%s&rn=%d&gsm=1e&1594447993172=' % (search, search, str(pn), self.__per_page)
            # 设置header防403
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=self.headers)
                page = urllib.request.urlopen(req)
                rsp = page.read()
            except UnicodeDecodeError as e:
                print(e)
                print('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                print(e)
                print("-----urlErrorurl:", url)
            except socket.timeout as e:
                print(e)
                print("-----socket timout:", url)
            else:
                # 解析json
                rsp_data = json.loads(rsp)
                self.save_image(rsp_data, word)
                # 读取下一页
                print("下载下一页")
                pn += 60
            finally:
                page.close()
        print("下载任务结束")
        return

    def start(self, word, total_page=1, start_page=1, per_page=30):
        """
        爬虫入口
        :param word: 抓取的关键词
        :param total_page: 需要抓取数据页数 总抓取图片数量为 页数 x per_page
        :param start_page:起始页数
        :param per_page: 每页数量
        :return:
        """
        self.__per_page = per_page
        self.__start_amount = (start_page - 1) * self.__per_page
        self.__amount = total_page * self.__per_page + self.__start_amount
        self.get_images(word)


if __name__ == '__main__':
    crawler = Crawler(0.05)  # 抓取延迟为 0.05

    crawler.start('美女', 10, 2, 10)  # 抓取关键词为 “美女”，总数为 1 页（即总共 1*60=60 张），开始页码为 2
    # crawler.start('二次元 美女', 10, 1)  # 抓取关键词为 “二次元 美女”，总数为 10 页（即总共 10*60=600 张），起始抓取的页码为 1
    # crawler.start('帅哥', 5)  # 抓取关键词为 “帅哥”，总数为 5 页（即总共 5*60=300 张）
