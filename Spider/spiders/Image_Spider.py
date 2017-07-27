# -*- coding: utf-8 -*-

import scrapy
import re

from scrapy.pipelines.images import ImagesPipeline
from Spider.items import SpiderItem

class Dahyun_Spider(scrapy.Spider):
    name = "Dahyun_Spider"

    start_urls = ['http://gall.dcinside.com/board/lists/?id=dahyeon&page=1&exception_mode=recommend']

    def parse(self, response):
        for post in response.css("td.t_subject"):
            next_post = post.css('a:not(.icon_notice)::attr(href)').extract_first()

            if next_post is not None:
                next_post = response.urljoin(next_post)
                yield scrapy.Request(next_post, callback = self.parse_img)

        next_page = response.css('div#dgn_btn_paging a.on+a::attr(href)').extract_first()
        
        if next_page is not None:
            next_post = response.urljoin(next_post)
            yield scrapy.Request(next_post, callback = self.parse)

    def parse_img(self, response):
        img_urls = 0
        for link in response.css('div.s_write'):
            img_urls = link.css('img::attr(src)').extract()
            for img_url in img_urls:
                img_url = img_url.replace('co.kr', 'com')

                p = re.compile(r'dcimg[0-9]+')
                m = p.search(img_url)

                if m is not None:
                    img_url = re.sub(r'dcimg[0-9]+', 'image', img_url)

                yield SpiderItem(file_urls = [img_url])
