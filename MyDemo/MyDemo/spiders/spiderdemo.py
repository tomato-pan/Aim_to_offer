from scrapy.spiders import Spider


class SpiderDemo(Spider):
    name = "spiderdemo"
    start_urls = ["http://woodenrobot.me"]

    def parse(self, response, **kwargs):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
