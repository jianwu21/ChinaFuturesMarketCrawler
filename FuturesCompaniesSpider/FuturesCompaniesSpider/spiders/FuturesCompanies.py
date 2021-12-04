# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import FuturesCompanyItem


class FuturescompaniesSpider(scrapy.Spider):
    name = 'FuturesCompanies'
    allowed_domains = ['www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']
    start_urls = ['http://www.cfachina.org/informationpublicity/futurescompanyinformantionpublicity/qhgsjbqk/']

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, "html5lib")
        div_mod_tables = soup.findAll('div', class_='mod-tables')
        tables = div_mod_tables[0].find('table')
        companyCodes = tables.findAll('tr')

        if div_mod_tables is not None:
            return

        pass
