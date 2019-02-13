import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):

  # Main Fields
  main_headline = Field()
  headline = Field()

  # Separate Fields
  url = Field()
  project = Field()
  spider = Field()
  server = Field()
  date = Field()

  # Location Fields
  # location = Field()

########################################

class TestItem(scrapy.Item):
  id = scrapy.Field()
  name = scrapy.Field()
  description = scrapy.Field()

########################################

class MovieItem(scrapy.Item):
# defining our item fields

  title = scrapy.Field()
  directors = scrapy.Field()
  writers = scrapy.Field()
  stars = scrapy.Field()
  popularity = scrapy.Field()

########################################