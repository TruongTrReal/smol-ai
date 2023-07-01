```python
import scrapy
from scrapy.http import FormRequest
from web_scraper.items import StockItem

class VietstockSpider(scrapy.Spider):
    name = 'vietstock'
    login_url = 'https://finance.vietstock.vn/login'
    start_urls = ['https://finance.vietstock.vn/doanh-nghiep-a-z']

    def parse(self, response):
        # extract stock data
        for stock in response.css('div.listing__data'):
            item = StockItem()
            item['symbol'] = stock.css('div.symbol::text').get()
            item['info'] = stock.css('div.info::text').getall()
            yield item

        # handle pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def start_requests(self):
        yield scrapy.Request(self.login_url, self.login)

    def login(self, response):
        # login
        return FormRequest.from_response(
            response,
            formdata={'email': 'kopoji3733@dotvilla.com', 'password': '123123'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        yield from super().start_requests()
```