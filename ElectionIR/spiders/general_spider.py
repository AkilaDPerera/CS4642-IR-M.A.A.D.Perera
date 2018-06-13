import scrapy

class QuotesSpider(scrapy.Spider):
    name = "general"

    start_urls = ['https://akiladperera.alwaysdata.net/']

    def parse(self, response):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(type(response))
        print(response.css('a').extract_first())
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        
        # with open(filename, 'wb') as f:
        #     f.writelines(response.css('a'))
        # self.log('Saved file %s' % filename)