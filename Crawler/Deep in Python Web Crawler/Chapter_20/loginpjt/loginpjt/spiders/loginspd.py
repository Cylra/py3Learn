# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request

class LoginspdSpider(scrapy.Spider):
    name = 'loginspd'
    allowed_domains = ['douban.com']
    #start_urls = ['https://accounts.douban.com/login']

    #设置header信息,用于模拟浏览器
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
    
    #重写了父函数,第一次会默认调用该方法中的请求
    def start_requests(self):
        #爬一次登录页,然后进入回调函数parse()
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback = self.parse)]

    #解析登录页面
    def parse(self, response):
        #获取验证码图片所在地址,captcha为一个list
        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()
        #登录时网页有时有验证码,有时候没有
        #需要做判断
        if len(captcha) > 0:
            print("此时有验证码")
            localpath = "captcha.jpg"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看本地图片captcha.jpg并输入对应验证码:")
            captcha_value = input()
            #设置要传递的post信息
            data = {
                "form_email": "287168219@qq.com",
                "form_password": "#####",
                #验证码字段
                "captcha-solution": captcha_value,
                #设置需要转向的网址,我们在此爬取个人中心页,所以转向个人中心页
                "redir": "https://www.douban.com/people/62172213/"
            }
        #无需验证码
        else:
            print("此时没有验证码")
            #设置要传递的post信息,没有验证码字段
            data = {
                "form_email": "287168219@qq.com",
                "form_password": "#####",
                "redir": "https://www.douban.com/people/62172213/"
            }
        print("登录中...")
        #通过FormRequest进行登录
        return [FormRequest.from_response(response, 
                meta={"cookiejar": response.meta["cookiejar"]}, 
                headers = self.header,
                #设置post表单中的数据
                formdata = data,
                #设置回调函数,此时回调函数为自定义函数next()
                callback = self.next)
                ]
        
    def next(self, response):
        print("此时已经登录完成并爬取了个人中心的数据")
        #此时response为个人中心网页中的数据
        #网页标题
        xtitle = "/html/head/title/text()"
        title = response.xpath(xtitle).extract()
        print("网页标题是:" + title[0])