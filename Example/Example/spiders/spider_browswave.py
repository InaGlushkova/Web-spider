# web spider

import scrapy
from Example.items_brs import VeloaccessorItem

import re

class BrowswaveSpider(scrapy.spiders.Spider):
  name = 'bricolage_spider'
  allowed_domains = ['mr-bricolage.bg']
  start_urls = ["https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=0",
                "https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=1",
                "https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=2"]


  def parse(self, response):
    
    for href in response.xpath("//div/a[@class='name']//@href"):

      url = 'https://mr-bricolage.bg' + href.extract()
      yield scrapy.Request(url, callback=self.parse_dir_contents)

    next_page_url = response.xpath("//ul[@class='pagination']/li[@class='active']/a/@href").extract_first()

    if next_page_url:
      next_page_url = response.urljoin(next_page_url)
      yield scrapy.Request(url=next_page_url, callback=self.parse)

  def parse_dir_contents(self, response):
    item = VeloaccessorItem()

    item['title'] = response.xpath("//div[@class='col-md-6']/h1/text()").extract()
    item['price'] = response.xpath("normalize-space(//div[@class='col-md-12 price']/p/text())").re(r"(\d+)")
    item['picture'] = response.xpath("//meta[@property='og:image']/@content").extract()
    item['characteristic'] = response.xpath("//meta[@property='og:description']/@content").extract()

    yield item
