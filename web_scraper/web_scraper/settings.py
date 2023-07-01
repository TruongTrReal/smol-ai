# Scrapy settings for web_scraper project

BOT_NAME = 'web_scraper'

SPIDER_MODULES = ['web_scraper.spiders']
NEWSPIDER_MODULE = 'web_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'web_scraper.pipelines.WebScraperPipeline': 300,
}

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# User Agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# Login Credentials
LOGIN_EMAIL = 'kopoji3733@dotvilla.com'
LOGIN_PASSWORD = '123123'

# Target URL
TARGET_URL = 'https://finance.vietstock.vn/doanh-nghiep-a-z'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'web_scraper.middlewares.WebScraperDownloaderMiddleware': 543,
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'web_scraper.middlewares.WebScraperSpiderMiddleware': 543,
}