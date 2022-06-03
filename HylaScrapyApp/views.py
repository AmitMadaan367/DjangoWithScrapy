# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import scrapy
from scrapy.crawler import CrawlerProcess
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import * 


data={}
all_data=[]

class ScrapyApi(APIView):
    def get(self, request, format=None):
        class HylaSpider(scrapy.Spider):
            print("first")
            name = 'hyla'
            # allowed_domains = ['hyla.com']
            # start_urls = ['http://hyla.com/']

            def start_requests(self):
                url ='https://qa.google.hylatest.com' 
                print("yaaa2")
                yield scrapy.Request(url=url, callback=self.parse)


            def parse(self, response):
                print("second")
                programdata = ProgramUrls.objects.all()
                all_urls=[]
                for check in programdata:
                    print(check.url,"check")
                    all_urls.append(check.url)
                # all_urls=[
                # 'https://qa.att.hylatest.com/info',
                # 'https://qa-freedom.canada.dls-test.com/info',
                # 'https://qa.google.hylatest.com/info',
                # 'https://qa-koodo.canada.dls-test.com/info',]
                for uri in all_urls:
                    yield scrapy.Request(url=uri, callback=self.get_data)

                

            def get_data(self, response):
                print("Third")
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
                output={"name":name,"commit_id":commit_id,"email":email,"branch":branch,"timestamp":timestamp}
                all_data.append(output)

        
            
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        print("final")

        process.crawl(HylaSpider)
        process.start()

        data.update({"data":all_data})
    
        return Response(data)


# python manage.py runserver --nothreading --noreload





