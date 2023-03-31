# BaiduImageSpider
百度图片爬虫，基于python3

个人学习开发用

单线程爬取百度图片。


顺带推荐一个付费好用的代理：[SmartProxy 全球IP代理](https://www.smartproxy.cn/regist?invite=HV8QHR)1亿真实住宅IP资源。
专业海外http代理商，千万优质纯净住宅IP资源，覆盖全球城市，高匿稳定提供100%原生住宅IP，支持社交账户，电商平台，网络数据收集等服务。
成功率伪装度超高！！本人测试用过之后感觉速度确实嘎嘎快，很给力。
搞跨境电商的用户可以用来tiktok养号，每个月还会更新一次代理IP池~
付费套餐多种多样，现在春季价格优惠，只要65折！
需要高质量代理IP的可以注册后联系客服，[实名注册后赠送500M流量](https://www.smartproxy.cn/regist?invite=HV8QHR)，不懂怎么用的同学可以问客服或者看视频教程。（官网有很多简单易懂的视频教学）

- 超高并发备份：独享高性能服务器，以真实住宅地址进行请求访问，保持代理正常连接，不限制并发数量，降低业务成本，提高运行效率。
- 优质IP资源：整合真实家庭住宅IP，汇聚IP资源池，不断更新IP，来自全球各个国家地区进行访问。自有数据节点，网络集成快捷。
- 形式多样：多种代理认证模式，帮助账户灵活设置，账密模式通过region参数添加制定国家城市；API白名单模式通过API链接获取即可。
- 技术服务：支持业务场景定制独享IP，千兆超高速带宽，出口IP可定制时效提供获取流量使用报告，追踪流量记录。  

<div align=center>
   <img src="https://user-images.githubusercontent.com/29977021/228770306-6c5d0b8a-c381-4be3-b500-e43fc47298b3.png" width="400px">
</div>

官网链接：https://www.smartproxy.cn/

专属注册链接：[https://www.smartproxy.cn/regist](https://www.smartproxy.cn/regist?invite=HV8QHR)

# 爬虫工具 Required

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

