# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TenementItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    origin_href = scrapy.Field()
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    create_at = scrapy.Field()
    update_at = scrapy.Field()
    oringin_images_urls = scrapy.Field()
    local_image_paths = scrapy.Field()



