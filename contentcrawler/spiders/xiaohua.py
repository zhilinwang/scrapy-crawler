#! /usr/env/bin python2.7
#coding=utf-8
import scrapy
import json
from scrapy.selector import Selector
from scrapy import log
from contentcrawler.items import Joke
class XiaohuaSpider(scrapy.Spider):
    name="xiaohua"
    allowed_domains=['zol.com.cn']
    start_urls=['http://xiaohua.zol.com.cn/']
    def parse(self,response):
        sel=Selector(response)
        url=response.url
        try:
            self.start_urls.index(url)
            sections=sel.xpath('//div[@class="main"]/div[@class="section classification-section"]/ul/li/a/@href').extract()
            log.msg("Sections length:%d ." %len(sections),level=log.INFO)
            for section in sections:
                strip_url=url.rstrip('/')
                full_path=strip_url+section
                log.msg("Crawler is crawlling path:%s ." %full_path,level=log.INFO)
                yield scrapy.Request(full_path,callback=self.parse)
        except:
            raw_jokes=sel.xpath('//ul/li[@class="article-summary"]')
            log.msg("Page joke count:%d" % len(raw_jokes),level=log.INFO)
            for raw_joke in raw_jokes:
                joke=Joke()
                title=raw_joke.xpath('span/a/text()').extract()[0]
                content=raw_joke.xpath('div[@class="summary-text"]/text()').extract()
                content=  '\n'.join(content)
                joke['title']=title
                joke['content']=content
                try:
                    next_page=sel.xpath('//div[@class="page-box"]/div/a[@class="page-next"]/@href').extract()[0]
                    if next_page is not None:
                        relative_path=next_page.split('/')[-1]
                        if url.endswith('.html'):
                            url=url.rstrip('/')
                            idx=url.rindex('/')
                            url=url[0:idx]
                        strip_url=url.rstrip('/')
                        full_path=strip_url+'/'+relative_path
                        yield scrapy.Request(full_path,callback=self.parse)
                except:
                    log.msg("Final page reached",level=log.INFO)
                yield joke
