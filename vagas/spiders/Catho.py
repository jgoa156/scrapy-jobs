# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'Catho'
    allowed_domains = ['www.catho.com.br']
    start_urls = ['https://www.catho.com.br/vagas/engenharia/manaus-am/?q=engenharia&cidade_id%5B0%5D=1222',
                  'https://www.catho.com.br/vagas/engenheiro/manaus-am/?q=engenheiro&cidade_id%5B0%5D=1222']

    def parse(self, response):
        for vaga in response.css("ul.sc-hZLPDR.hqFBOt.gtm-class li"):
            titulo = str(
                vaga.css("header h2 a::text").extract_first())
            link = str(
                vaga.css("header h2 a::attr(href)").extract_first())

            yield {'titulo': titulo,
                   'fonte': 'Catho',
                   'link': link}

            print("\n")
