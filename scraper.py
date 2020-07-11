import scrapy

class SidScraper(scrapy.Spider):
    name    =   "sidspider"
    start_urls  =   ['https://sidyzworld.wordpress.com/category/malayalam-movie-views/']

    def parse(self,response):
        SET_SELECTOR    =   '.post post-4886 type-post status-publish format-standard hentry category-malayalam-movie-views has-post-thumbnail fallback-thumbnail'
        for review in response.css(SET_SELECTOR):
            NAME_SELECTOR   =   'h2::text'
            yield{
                'name': review.css(NAME_SELECTOR).extract_first(),
            }