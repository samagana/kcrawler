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
        listofurls = response.css(
            'div.tab_content div.content a::attr(href)').getall()
        for i in range(len(listofarticles)):
            item['url'] = 'https://vijaykarnataka.com' + listofurls[i]
            item['content'] = ""
            item["headline"] = listofarticles[i]
            yield item
