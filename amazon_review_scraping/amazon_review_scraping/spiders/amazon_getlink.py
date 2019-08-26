# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonReviewScrapingItem

class AmazonGetlinkSpider(scrapy.Spider):
    name = 'amazon_getlink'
    start_urls = ['https://www.amazon.com/s?i=photo&bbn=14241151&rh=n%3A172282%2Cn%3A493964%2Cn%3A502394%2Cn%3A7161091011%2Cn%3A898400%2Cn%3A14241151%2Cp_85%3A2470955011&dc&page=1&fst=as%3Aoff&qid=1566770500&rnid=2470954011&ref=sr_pg_2']

    def parse(self, response):
        items = AmazonReviewScrapingItem()

        product_links = response.css('.a-color-base.a-text-normal::attr(href)').extract()
        product_names = response.css('.a-color-base.a-text-normal::text').extract()

        items['product_links'] = product_links
        items['product_names'] = product_names

        yield items
