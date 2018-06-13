import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "general"

    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        body = response.body
        soup = BeautifulSoup(body)

        # Saving the page
        page = response.url.split("/")[-2]
        filename = 'data/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(body)
        self.log('Saved file %s' % filename)

        # Extracting links
        links = soup.find_all('a')
        for link in links:
            next_route = link.get('href')
            yield response.follow(next_route, callback=self.parse)