# BaiduImageSpider
百度图片爬虫，基于python3

个人学习开发用

单线程爬取百度图片

# Required

**需要安装python版本 >= 3.6**

# 使用方法
```
$ python crawling.py -h
usage: crawling.py [-h] -w WORD -tp TOTAL_PAGE -sp START_PAGE
                   [-pp [{10,20,30,40,50,60,70,80,90,100}]] [-d DELAY]

optional arguments:
  -h, --help            show this help message and exit
  -w WORD, --word WORD  抓取关键词
  -tp TOTAL_PAGE, --total_page TOTAL_PAGE
                        需要抓取的总页数
  -sp START_PAGE, --start_page START_PAGE
                        起始页数
  -pp [{10,20,30,40,50,60,70,80,90,100}], --per_page [{10,20,30,40,50,60,70,80,90,100}]
                        每页大小
  -d DELAY, --delay DELAY
                        抓取延时（间隔）
```

开始爬取图片
```
python crawling.py --word "美女" --total_page 10 --start_page 1 --per_page 30
```


另外也可以在`crawling.py`最后一行修改编辑查找关键字
图片默认保存在项目路径
运行爬虫：
``` python
python crawling.py
```

# 博客

[爬虫总结](http://www.jwlchina.cn/2016/02/06/python%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87%E7%88%AC%E8%99%AB/)

效果图：
![效果图](http://blog-image.jwlchina.cn/kong36088/kong36088.github.io/master/uploads/python%E5%9B%BE%E7%89%87%E7%88%AC%E8%99%AB%E6%88%AA%E5%9B%BE.png)

# 捐赠

您的支持是对我的最大鼓励！
谢谢你请我吃糖
![wechatpay](http://blog-image.jwlchina.cn/kong36088/kong36088.github.io/master/uploads/site/wechat-pay.png)
![alipay](http://blog-image.jwlchina.cn/kong36088/kong36088.github.io/master/uploads/site/zhifubao.jpg)

