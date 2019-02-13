# Scrapy 4th

import scrapy
from scrapy.http import Response

class TestSpider(scrapy.Spider):
  name = 'practical_spider'
  allowed_domains = ['superdatascience.com']
  start_urls = ['https://www.superdatascience.com/scrapy_practical/']

  def parse(self, response):
    item = {
            'logo': response.css('#header > div > div > a > img').xpath('@src').extract_first(), 
            'Q1': response.css('#content > div.entry-content > h3.sc1::text').extract_first(),
            'Q1.1': response.css('#content > div.entry-content > h3:nth-child(7)::text').extract_first(),
            'Q2': response.css('#content > div.nth-child(4) > p::text').extract_first(),
            'list_items': [
              e for e in 
              response.css('#content > div.third-challenge > ul *::text').extract() if e.strip()
            ],
    }

    self.logger.info('aaa %s', item)
    return item
