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
        soup = BeautifulSoup(html, "html.parser")
        div_mod_tables = soup.find('div', class_='mod-tables')
        tables = div_mod_tables.findAll('tbody', id='tbody')
        companyCodes = tables.findAll('td', class_='b-cnt1')

        for companyCode in companyCodes:
            code = companyCode.text
        
        if div_mod_tables is not None:
            return

        pass
