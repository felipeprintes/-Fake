# -*- coding: utf-8 -*-
import scrapy
from lenotg1.items import Lenotg1Item


class Lenotg1Spider(scrapy.Spider):
    name = 'Lenotg1'
    allowed_domains = ['g1.globo.com/tudo-sobre/bndes']
    start_urls = ['http://g1.globo.com/tudo-sobre/bndes/']

    def parse(self, response):
        titulos = Lenotg1Item( {
        	"url": response.url,
        	#"title": response.xpath("//body/descendant-or-self::*[(self::h1 or self::h1 or self::h3 or self::a or self::p)and re:test(@class,'.*feed.*')]/text()").extract()
        	"title": self.to_str(response.xpath("//body/descendant-or-self::*[(self::h1 or self::h1 or self::h3 or self::a or self::p)and re:test(@class,'.*feed.*')]/text()")),
        	#"resumo": "".join(response.xpath("//body/descendant-or-self::*[re:test(@class, '.*_.*')]/text()").extract()),
        	"resumo": self.to_str(response.xpath("//body/descendant-or-self::*[re:test(@class, '.*_.*')]/text()")),
        	#"links": response.xpath("//div[@class='bastian-feed-item']//@href").extract(),
        	"links": self.to_str(response.xpath("//div[@class='bastian-feed-item']//@href")),
        	#"tags": response.xpath("//ul[@class='entities__list']//li//text()").extract()
        	"tags": self.to_str(response.xpath("//ul[@class='entities__list']//li//text()"))
        })
        return titulos

    def to_str(self, element):
    	return "\¬".join(element.extract())
