#!/usr/local/env python3
# -*- coding: utf-8 -*-

from scrapy.spider import Spider, Request
import json
import os
from acgstay.util_helper import util_helper


class AcgstaySpider(Spider):

    name = 'acgstay'
    allow_domains = 'acagnavi.com'
    start_urls = [
        'https://a1.acgnavi.com:8440/index?index=mainindex&isv=0&mode=21&sign=CB7165890EB8416AB4766C23907BA8C1E2CAEAC1AFA26E2BBD6BF9B2B560000E'
    ]

    def parse(self, response):
        infos = json.loads(response.body)
        indexes = infos['indexes']
        for each in indexes:
            url = each['url']
            index = each['index']
            des = each['des']
            new_url = url.split('/')
            filename = new_url.pop()
            url_head = '/'.join(new_url)
            filename_s = filename.split('_')
            filename_s.pop()
            filename_head = '_'.join(filename_s)

            index_filename = des + '_' + index
            pathname = os.path.abspath(os.path.join(
                os.path.dirname(__file__), "../imgs/" + index_filename))

            if  not os.path.exists(pathname):
                os.mkdir(pathname)

            for i in range(1, 10000):
                i_s = str(i).zfill(4)
                img_name = filename_head + '_' + i_s + '.JPG'
                img_url = url_head + '/' + img_name

                helper = util_helper()
                img_stream = helper.curl_get(img_url)
                if img_stream:
                    file_obj = open(pathname + '/' + img_name, 'wb')
                    file_obj.write(img_stream)
                    file_obj.close

