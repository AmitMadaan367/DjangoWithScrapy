import scrapy
from scrapy.crawler import CrawlerProcess


class HylaSpider(scrapy.Spider):
    name = 'hyla'
    # allowed_domains = ['hyla.com']
    # start_urls = ['http://hyla.com/']

    def start_requests(self):
        url ='https://qa.google.hylatest.com' 
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        all_urls=[
        'https://qa.att.hylatest.com/info',
        'https://qa-freedom.canada.dls-test.com/info',
        'https://qa.google.hylatest.com/info',
        'https://qa-koodo.canada.dls-test.com/info',]
        for uri in all_urls:
            yield scrapy.Request(url=uri, callback=self.get_data)

        

    def get_data(self, response):
        data=response.json()
        print(data)
        print("----------------------------")
        name=data['git']['build']['user']['name']
        commit_id=data['git']['commit']['id']
        email=data['git']['build']['user']['email']
        branch=data['git']['branch']
        timestamp=data['git']['commit']['time']
        print("name",name)
        print("commit_id",commit_id)
        print("email",email)
        print("branch",branch)
        print("timestamp",timestamp)

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(HylaSpider)
    process.start()

