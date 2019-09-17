import scrapy
from scrapy.crawler import CrawlerProcess

class MailinatorSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'https://www.mailinator.com/v3/index.jsp?zone=public&query=otheradult#/#inboxpane',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("=").split("#/#")[0]
        filename = 'quotes-%s.html' % page



    process = CrawlerProcess(
        settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'items.json'
        }
    )

process.crawl(MySpider)
process.start()