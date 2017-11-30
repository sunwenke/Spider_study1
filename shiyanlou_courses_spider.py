# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for course in response.css('li.public'):
            yield {
                'name': course.css('div.d-inline-block a::text').extract_first().strip(),
                'update_time': course.css('div.mt-2 relative-time::attr(datetime)').extract_first()
            }



