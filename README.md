# Recuperação de Informações
Professor: Me. Júlio César Batista
Descrição: 
Conceito de crowdsourcing. Ferramentas de análise, monitoramento e
benchmark. Algoritmos e soluções para problemas de busca e extração
de informação. Web mining. Web crawling. Text Mining.

data: 01/02/2020
Github:https://github.com/ejulio/pos132_cmp1101_recuperacao_informacoes


##
https://regex101.com/

https://regex101.com/r/2Lv5Pj/2

### sintax
[] -> or
- -> range
\s -> espaço
. -> qualquer coisa
() -> define um grupo
\d -> digito
\w -> letras


### exemplo

regex: [0-9]\.\s[a-zA-Z\s]+\([0-9]+\)
validação: 2. Pride and Projudice by Jane Austen (1302)

regex: (\d)\.\s([\w\s]+)\sby\s([\w\s]+)\((\d+)\)
Validação: 2. Pride and Projudice by Jane Austen (1302)

Match 1
Full match	0-44	2. Pride and Projudice by Jane Austen (1302)
Group 1.	0-1	2
Group 2.	3-22	Pride and Projudice
Group 3.	26-38	Jane Austen 
Group 4.	39-43	1302

#### Nomear valores
(?<pos>\d)\.\s([\w\s]+)\sby\s([\w\s]+)\((\d+)\)
2. Pride and Projudice by Jane Austen (1302)

Match 1
Full match	0-44	2. Pride and Projudice by Jane Austen (1302)
Group `pos`	0-1	2
Group 2.	3-22	Pride and Projudice
Group 3.	26-38	Jane Austen 
Group 4.	39-43	1302


#### Ignorar espaços antes do by

(?<pos>\d)\.\s*([\w\s]+?)\s+by\s+([\w\s]+)\((\d+)\)

2. Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice    by     Jane Austen (1302)


#### Caracteres

(?<pos>\d+)\.\s*([\w\s,.:;]+?)\s+by\s+([\w\s]+)\((\d+)\)
2. Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice    by     Edgar(1302)
2. Edgar , The Raven    by     Jane Austen (1302)
12. 1983 by George Orwell (1302)

#### Tem que começar e acabar com isso

^(?<pos>\d+)\.\s*([\w\s,.:;]+?)\s+by\s+([\w\s]+)\((\d+)\)$


2. Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice by Jane Austen (1302)
2.       Pride and Projudice    by     Edgar(1302)
2. Edgar , The Raven    by     Jane Austen (1302)
12. 1983 by George Orwell (1302)
X = no ranking do gutenberge 12. 1983 by George Orwell (1302)
X = 12. 1983 by George Orwell (1302)no ranking do gutenberge 


#### Autor desconhecido

^(?<pos>\d+)\.\s*([\w\s,.:;\-]+?)\s+(by\s+([\w\s]+?)\s*)?\((\d+)\)$
5. Beowulf: An Anglo-Saxon Epic Poem (815)

Match 6
Full match	346-388	5. Beowulf: An Anglo-Saxon Epic Poem (815)
Group `pos`	346-347	5
Group 2.	349-382	Beowulf: An Anglo-Saxon Epic Poem
Group 5.	384-387	815

#### Ignorando o by 

^(?<pos>\d+)\.\s*([\w\s,.:;\-]+?)(?:\s+by\s+([\w\s]+?)\s*)?\((\d+)\)$
2. Pride and Projudice by Jane Austen (1302)

Match 1
Full match	0-44	2. Pride and Projudice by Jane Austen (1302)
Group `pos`	0-1	2
Group 2.	3-22	Pride and Projudice
Group 3.	26-37	Jane Austen
Group 4.	39-43	1302

#### Validando datas
Expr: ^(\d{1,2})\/(\d{1,2})\/(\d{2}|\d{4})$
validar: 
01/01/2019
1/1/2020
01/1/2020
1/01/2020
01/01/20
1/1/20
01/1/20
1/01/20

## Processo de markov

Grafos para fazer previsão, cada minho tem um peso,
usando o peso mais provabilistico é possível gera textos aleatórios.

Ver imagem 1 e 2.

exemplo: https://kingjamesprogramming.tumblr.com/


## scrapy

http://quotes.toscrape.com/

https://github.com/rennerocha

### html

$('.quote') -> primeira class

$$('.quote') ->  todas as classes

$('#productTitle').innerText -> busca pelo id

$$('a[class=tag]') -> tag a com clas

### scrapy

pip install scrapy

http://quotes.toscrape.com/

scrapy shell 

Carregar a página
fetch('http://quotes.toscrape.com/')
 
//mostrar o response
response

//ver a página baixada 
view(response) 

//pegar o conteúdo
//::text seletor especial para pegar o conteúdo da tag
response.css('.text::text').get()

//pegr todos 
response.css('.text::text').getall()

//autor
response.css('.author::text').get()
'Albert Einstein'

>>> response.css('.author::text').getall()
['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']


//posicional
response.css('.quote')[0].css('.author::text').get()

//rodar e salvar o resultado em json
// -o aquivo.extensão a extensão é gerada sozinha
scrapy runspider quote_spider.py -o quote.json

//proximo irmão
aboutHref = quote.css('.author + a::attr(href)').get()

// links igual não são rechamados
'dupefilter/filtered': 50,
'item_scraped_count': 50

em dev para fazer um cache, assim não vai.
scrapy runspider quote_spider.py -o quote.json -S HTTPCACHE_ENABLED=1




