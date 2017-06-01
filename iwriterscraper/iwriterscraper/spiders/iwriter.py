# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

class IwriterSpider(BaseSpider):
    name = 'iwriter.com'
    start_urls = ['https://www.iwriter.com/login.php']

    def parse(self, response):
        return [FormRequest.from_response(response,
                    formdata={'username': 'username', 'password': 'secret'},
                    callback=self.after_login)]

        def after_login(self, response):

	    if "authentication failed" in response.body:
	        self.log("Login failed", level=log.ERROR)
	        return
	    # We've successfully authenticated, let's have some fun!
	    else:
	        return Request(url="http://www.example.com/tastypage/",
	               callback=self.parse_tastypage)
	
	def parse_tastypage(self, response):
	    hxs = HtmlXPathSelector(response)
	    yum = hxs.select('//img')
	
    