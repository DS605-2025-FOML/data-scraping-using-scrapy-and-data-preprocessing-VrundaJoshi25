import scrapy


class BooksScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    rating = scrapy.Field()
    product_page_url = scrapy.Field()