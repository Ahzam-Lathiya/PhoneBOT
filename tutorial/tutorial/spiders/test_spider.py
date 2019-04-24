import scrapy
from ..items import TutorialItem


class test_spider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
    'https://www.kuz.com.au/'
                 ]              
    
    def parse(self, response):
        items=TutorialItem()
        
        all_div_quotes = response.css('div.featured-content')
        
        for quotes in all_div_quotes:
            mob=quotes.xpath('//div[@class=$val]/h4/a/text()', val='mob-name').extract()
    
            items['mob']=mob
    
            yield items

