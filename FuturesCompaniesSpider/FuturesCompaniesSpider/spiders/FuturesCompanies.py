# -*- coding: utf-8 -*-
import scrapy
from ..items import FuturesCompanyItem


class FuturescompaniesSpider(scrapy.Spider):
    name = 'FuturesCompanies'
    allowed_domains = ['www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']
    start_urls = ['http://www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']

    def parse(self, response):
        html = response.text

        print(html)
        pass
