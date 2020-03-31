# -*- coding: utf-8 -*-
import scrapy
from all.items import BiquItem
from scrapy import Request
from urllib import parse
from scrapy_redis.spiders import RedisSpider
'''分布式改造1.将scrapy.Spider变成scrapy_redis.spidres.RedisSpider;或则scrapy.CrwalSpider
变成scrapy_redis.spiders.RedisCrawlSpider。2.将爬虫中的start_urls删除。
增加一个redis_key="xxx"
这个redis_key是为了以后在redis中控制爬虫启动的。爬虫的第一个url，就是
redis中通过这个发送的。
3.将request存储在redis中：SCHEDULER="scrapy_redis.scheduler.Scheduler"
确保所有爬虫共享相同的去重指纹DUPEFILTER_CLASS="scrapy_redis.dupefilter.RFPDupeFilter"
设置redis为item pipeline：ITEM_PIPELINE={
'scrapy_redis.pipelines.RedisPipeline':300
}
续爬：SCHEDULER_PERSIST = True
设置连接：REDIS_HOST= '127.0.0.1'
PORT = 6379
password = 123456

'''

class BiquSpiderSpider(RedisSpider):
    name = 'biqu_spider'
    allowed_domains = ['vipzw.com']
    # start_urls = ['http://www.vipzw.com/map/1.html']
    redis_key = 'biqu'
    custom_settings = {'DEFAULT_REQUEST_HEADERS': {
                            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'Accept-Encoding':'gzip, deflate',
                            'Accept-Language':'zh-CN,zh;q=0.9',
                            'Cache-Control':'max-age=0',
                            'Connection':'keep-alive',
                            'Cookie':'Hm_lvt_ab3c0de16bd108959c9d601fa1f6967e=1585295492; clickbids=64925%2C171%2C56%2C103799%2C30505%2C103105; Hm_lpvt_ab3c0de16bd108959c9d601fa1f6967e=1585299264',
                            'Host':'www.vipzw.com',
                            'If-None-Match':'W/"5e70174f-3dcf"',
                            'Referer':'http://www.vipzw.com/103_103799/',
                            'Upgrade-Insecure-Requests':'1',
                            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }
    }



    def parse(self, response):
        #全网小说起始点
        xiaosuo_start_url = response.xpath("//ul/li/a/@href").extract()

        #获取每部小说url
        for xiaoshuo in xiaosuo_start_url:

            yield scrapy.Request(xiaoshuo,callback=self.page_page)
    def page_page(self,response):

        #目录页解析
        first_page = response.xpath("//dl/dd[10]/a/text()").extract()
        first_page = ''.join(first_page).replace(' ','')
        print(first_page)
        #小说名字
        story_name = response.xpath("//div[@id='info']/h1/text()").extract_first()
        #作者
        write = response.xpath("//div[@id='info']/p/text()").extract_first()
        write = ''.join(write).replace(' ','')



        if '第一章' in first_page:
            first_page_url = response.xpath('//dl/dd[10]/a/@href').extract()
            res = ''.join(first_page_url)
            res = parse.urljoin('http://www.vipzw.com/',res)
            req = Request(res,callback=self.deta_page)
            #将名字和作者传给content
            req.meta['na'] = story_name
            req.meta['work'] = write


            print('第一章url：',res)
            yield req




    def deta_page(self,response):
        #详情解析
        item = BiquItem()
        content = response.xpath("//div[@id='content']//text()").extract()
        content = ''.join(content).replace(' ','').replace('\n','')
        item['story_content'] = content.replace('\r','')
        page_name = response.xpath("//div[@class='bookname']/h1/text()").extract()
        item['story_page'] = page_name
        #翻页
        next_link =response.xpath("//div[@class='bottem1']/a[4]/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('http://www.vipzw.com/' + next_link,callback=self.deta_page)
        try:
            item['story_name'] = response.meta['na']
            item['story_writer'] = response.meta['work']
        except:
            item['story_name'] = ''
            item['story_writer'] = ''

        yield item

