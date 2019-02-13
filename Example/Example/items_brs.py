import scrapy
from scrapy.item import Item, Field

########################################

class VeloaccessorItem(scrapy.Item):
# defining our item fields

  title = scrapy.Field()
  price = scrapy.Field()
  picture = scrapy.Field()
  characteristic = scrapy.Field()

########################################