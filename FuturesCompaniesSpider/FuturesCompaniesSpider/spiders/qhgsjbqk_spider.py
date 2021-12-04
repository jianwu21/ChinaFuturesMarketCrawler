# -*- coding: utf-8 -*-
import scrapy
from ..items import FuturescompaniesspiderItem


class QhgsjbqkSpiderSpider(scrapy.Spider):
    name = 'qhgsjbqk_spider'
    allowed_domains = ['www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']
    start_urls = ['http://www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']

    def parse(self, response):
        pass
