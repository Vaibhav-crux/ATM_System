import scrapy
from ..items import LetsdoItem

class noon_one(scrapy.Spider):
    name = 'noon'
    page_number = 10
    start_urls = [
        'https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA%2C+United+States&start=0'
    ]

    def parse(self, response):
        items = response.css("div.kGIqQP")
        for i in items:
            title = i.css('..css-1m051bw::text').get()
            ratings = i.css('.css-chan6m::text').get()
            cost = i.css('.css-qgunke::text').get()

            item = LetsdoItem()
            item['title'] = title
            item['reatings'] = ratings
            item['cost'] = cost
            yield item

        next_page = f'https://www.yelp.com/search?find_desc=&find_loc=San+Francisco%2C+CA%2C+United+States&start={noon_one.page_number}'
        if noon_one.page_number <= 5:
            noon_one.page_number += 10
            yield response.follow(next_page, callback=self.parse)