#!/usr/bin/env python3
# encoding: utf-8
#使用scrapy api 在一个进程中同时运行多个spider

from tenement.spiders.anjuke import AnjukeSpider
from tenement.spiders.douban import DoubanSpider
from tenement.spiders.fang import FangSpider
from tenement.spiders.ganji import GanjiSpider
from tenement.spiders.lianjia import LianjiaSpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# process.crawl(AnjukeSpider)
# process.crawl(DoubanSpider)
# process.crawl(FangSpider)
# process.crawl(GanjiSpider)
process.crawl(LianjiaSpider)

process.start()

