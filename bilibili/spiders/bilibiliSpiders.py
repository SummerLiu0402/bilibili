from email import header
import scrapy
from ..items import BilibiliItem
class bilibiliSpiders(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['https://www.bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all',
                  "https://www.bilibili.com/v/popular/rank/bangumi",
                  "https://www.bilibili.com/v/popular/rank/movie",
                  "https://www.bilibili.com/v/popular/rank/car"]

    def parse(self, response):
       tail = response.url.split('/')[-1]
       rank_type = tail.split('?')[0]
       ul = response.xpath("//ul[contains(@class,'rank-list')]")
       for sel in ul.xpath(".//li"):
           item = BilibiliItem()
           item['type'] = rank_type
           item['title']= sel.xpath(".//a[contains(@class,'title')]/text()").extract()
           item['rank'] = sel.xpath(".//@data-rank").extract()
           item['play'] = sel.xpath(".//span[img[contains(@alt,'play')]]/text()").extract()
           item['like'] = sel.xpath(".//span[img[contains(@alt,'like')]]/text()").extract()
           item['up'] = sel.xpath(".//span[img[contains(@alt,'up')]]/text()").extract()
           item['follow'] = sel.xpath(".//span[img[contains(@alt,'follow')]]/text()").extract()
           yield item 