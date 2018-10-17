# -*- coding: utf-8 -*-
import scrapy
from lenotg1.items import Lenotg1Item
from scrapy.http import Request


class Lenotg1Spider(scrapy.Spider):
    name = 'Lenotg1'
    #allowed_domains = ['g1.globo.com/']
    start_urls = ['https://g1.globo.com/tudo-sobre/bndes']
    
    def parse(self, response):
        #for i in response.xpath("//div[@class='bastian-feed-item']//a"):
        urls = response.xpath("//div[@class='bastian-feed-item']//a//@href").extract()
        for i in urls:
            yield response.follow(i, self.parse_article)

        
        next_page = response.xpath("//*[@id='feed-placeholder']/div/div/div[3]/a/@href").extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
		
    def parse_article(self, response):
    
    	# titulos = Lenotg1Item( {
     #    	#"title": self.to_str(response.xpath("//body/descendant-or-self::*[(self::h1 or self::h1 or self::h3 or self::a or self::p)and re:test(@class,'.*feed.*')]/text()")),
     #    	#"title_resumo": self.to_str(response.xpath("//body/descendant-or-self::*[(self::h1 or self::h1 or self::h3 or self::a or self::p)and re:test(@class,'.*feed.*')]/text()")),
     #    	#"resumo": "".join(response.xpath("//body/descendant-or-self::*[re:test(@class, '.*_.*')]/text()").extract()),
     #    	#"resumo": self.to_str(response.xpath("//body/descendant-or-self::*[re:test(@class, '.*_.*')]/text()")),
     #    	#"links": response.xpath("//div[@class='bastian-feed-item']//@href").extract(),
     #    	#"links": self.to_str(response.xpath("//div[@class='bastian-feed-item']//a//@href")),
     #    	#"tags": response.xpath("//ul[@class='entities__list']//li//text()").extract()
     #    	"tags": self.to_str(response.xpath("//ul[@class='entities__list']//li//text()"))
     #    })
    	# #self.print_item(titulos)
    	# return titulos
       
        tags = self.to_str(response.xpath("//ul[@class='entities__list']//li//text()"))
        title = self.to_str(response.xpath("//h1[@class='content-head__title']//text()"))
        resumo = self.to_str(response.xpath("//h2[@class='content-head__subtitle']//text()"))
        
        titulos = Lenotg1Item(tags = tags, title = title, resumo = resumo)
        yield titulos

    def to_str(self, element):
        return ";".join(element.extract())
