# -*- coding: utf-8 -*-
import scrapy
from tenement.items import TenementItem
import time


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["m.lianjia.com"]
    start_urls = [
        'https://m.lianjia.com/hz/zufang/wenjiao/pg1',
        'https://m.lianjia.com/hz/zufang/wenjiao/pg2',
        'https://m.lianjia.com/hz/zufang/wenjiao/pg3',
    ]

    def parse(self, response):
        for sel in response.xpath('//li[@class="pictext"]'):
            item = TenementItem()
            item['title'] = sel.xpath('.//div[@class="item_list"]/div[1]/text()').extract_first().strip()
            item['price'] = sel.xpath('.//div[@class="item_list"]/div[@class="item_minor"]/div[2]').re(r'\d+')[0]
            item['origin_href'] = 'https://m.lianjia.com' + sel.xpath('./a/@href').extract_first()
            item['origin'] = 'lianjia'
            item['create_at'] = int(time.time())
            yield scrapy.Request(url=item['origin_href'], meta={'item': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['item']
        item['location'] = response.xpath('.//div[@class="location_desc"]/text()').extract_first().split('：')[-1].strip()
        item['origin_id'] = response.url.split('/')[-1].split('.')[-2]
        url_list = response.xpath('//ul[@class="pic_lists flexbox"]/li[@class="box_col"]/img/@origin-src').extract()
        if url_list:
            item['oringin_images_urls'] = url_list
        else:
            item['oringin_images_urls'] = []
        yield item


