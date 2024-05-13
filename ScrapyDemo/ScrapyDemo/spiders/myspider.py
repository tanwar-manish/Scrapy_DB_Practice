import scrapy
from ScrapyDemo.items import ProductItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['aoneplus.com']
    start_urls = ['https://aoneplus.com/product-category/computers-laptops/laptops/']

    def parse(self, response):
        product_titles = response.xpath('//*[@id="tokoo-shop-view-content"]/ul/li/div/div/div[2]/a/h2/text()').getall()
        product_prices = response.xpath('//*[@id="tokoo-shop-view-content"]/ul/li/div/div/div[3]/span/span/bdi/text()').getall()

        for title, price in zip(product_titles, product_prices):
            item = ProductItem()
            item['title'] = title.strip()
            item['price'] = price.strip()
            yield item
            # yield {
            #     'Title': title.strip(),
            #     'Price': price.strip()
            # }
