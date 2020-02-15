import scrapy


# scrapy runspider books_spider.py -o bookx.json
class BooksSpider(scrapy.Spider):
    name = 'books.toscrape.com'
    start_urls = ['http://books.toscrape.com/']

    index = 0;
    def parse(self, response):
        for link in response.css('h3 > a::attr(href)'):
            hrefBook = response.urljoin(link.get())
            self.index += 1
            yield scrapy.Request(hrefBook,
                                 callback=self.parse_book,
                                 meta={
                                     'dados': {
                                         'index': self.index,
                                         'url': hrefBook
                                     }
                                 })

            href = response.css('.next > a::attr(href)').get()
            if href:
                # follow por padrão vai para o parser
                # yield response.follow(href)
                yield response.follow(href, callback=self.parse)

    def parse_book(self, response):
        nome = response.css('h1::text').get()
        descricao = response.css('#product_description + p::text').get()
        valor = response.css('H1 + p[class=price_color]::text').get()
        # Pega a última posição
        categoria = response.css('.breadcrumb > li > a::text')[-1].get()
        print(categoria)
        dados = response.meta['dados']
        dados['nome'] = nome
        dados['descricao'] = descricao
        dados['valor'] = valor[1:]
        dados['moeda'] = valor[0]
        dados['categoria'] = categoria
        return dados

# scrapy runspider quote_spider.py
