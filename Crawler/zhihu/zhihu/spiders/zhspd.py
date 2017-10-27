# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class ZhspdSpider(scrapy.Spider):
    name = 'zhspd'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com']
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Connection": "keep-alive",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }
    def start_requests(self):
        url = "https://login.sina.com.cn/signup/signin.php?entry=sso"
        yield Request(url, headers = self.headers, callback=self.login)
    
    def login(self, response):
        with open("login.html", "wb") as f:
            f.write(response.body)

        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract_first()
        #print(xsrf)
        post_url = "https://www.zhihu.com/login/email"
        post_data = {
            "_xsrf": xsrf,
            "email": "287168219@qq.com",
            "password": "123456"
        }
        return (FormRequest.from_response(response, url=post_url, formdata =post_data, headers = self.headers, callback = self.parse))

    def parse(self, response):
        with open("afterlogin.html", "wb") as f:
            f.write(response.body)
