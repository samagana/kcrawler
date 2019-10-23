import scrapy
from kcrawler.items import KcrawlerItem


class MainSpider(scrapy.Spider):
    name = 'mainspider'

    def __init__(self, *args, **kwargs):
        self.keyword = kwargs.get('keyword')
        self.unique_id = kwargs.get('uid')
        self.start_urls = [
            'https://vijaykarnataka.indiatimes.com/topics/%s' % self.keyword]
        super(MainSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = KcrawlerItem()
        listofarticles = response.css(
            'div.tab_content div.content span.title::text').getall()
        for i in listofarticles:
            item['url'] = ""
            item['content'] = ""
            item["headline"] = i
            yield item
