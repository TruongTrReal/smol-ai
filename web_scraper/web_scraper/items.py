```python
import scrapy

class VietstockItem(scrapy.Item):
    # define the fields for your item here like:
    stock_symbol = scrapy.Field()
    stock_info = scrapy.Field()
```