import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes.toscrapy.com'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('.quote'):
            frase = quote.css('.text::text').get()
            autor = quote.css('.author::text').get()
            hrefAbout = quote.css('.author + a::attr(href)').get()
            # follow concata com o nome do dominnio
            hrefAbout = response.urljoin(hrefAbout)

            yield scrapy.Request(hrefAbout,
                                 callback=self.parse_autor,
                                 #força a releitura de uma página
                                 dont_filter=True,
                                 meta={
                                     'dados': {
                                         'frase': frase,
                                         'autor': autor
                                     }
                                 })

        # classe dentro da tag com o atributo
        href = response.css('.next a::attr(href)').get()
        if href:
            # follow por padrão vai para o parser
            # yield response.follow(href)
            yield response.follow(href, callback=self.parse)

    def parse_autor(self, response):
        data = response.css('.author-born-date::text').get()
        dados = response.meta['dados']
        dados['data'] = data
        return dados

# scrapy runspider quote_spider.py
