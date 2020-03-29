import scrapy
import re
import html2text

html2text.config.UNICODE_SNOB = True
html2text.config.BODY_WIDTH = 100000000000
html2text.config.SKIP_INTERNAL_LINKS = True
html2text.config.INLINE_LINKS = False
html2text.config.DECODE_ERRORS = 'strict'

com_formatacao = html2text.HTML2Text(bodywidth=html2text.config.BODY_WIDTH)
sem_formatacao = html2text.HTML2Text(bodywidth=html2text.config.BODY_WIDTH)
sem_formatacao.ignore_emphasis = True


class ArquivoPessoaSpider(scrapy.Spider):
    name = 'ArquivoPessoa'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_processados = 0

    def start_requests(self):
        for i in range(4600):
            yield scrapy.Request(url='http://arquivopessoa.net/textos/' + str(i), meta={'id': i})

    def parse(self, resposta):
        conteudo = resposta.css('#c1l4i1 > .content')

        def get_formatado(classe, tm=com_formatacao):
            item = conteudo.css(classe).get()
            if not item:
                return ''
            # Subtituir parágrafos vazios por linhas em branco
            item = re.sub(r'\s*(?:<p>\s*<\/p>|<p\s*\/>)\s*', '<br/>', item)
            # Converter de html para texto
            return tm.handle(item).strip().replace('\n\n', '\n')

        def get_simples(classe):
            return get_formatado(classe, tm=sem_formatacao).strip('#').strip()

        prosa = get_formatado('.texto-prosa')
        poesia = get_formatado('.texto-poesia')

        if prosa:
            text = prosa
            tipo = 'prosa'
        else:
            text = poesia
            tipo = 'poesia'

        dados = {
            'id': resposta.meta['id'],
            'autor': get_simples('.autor'),
            'titulo': get_simples('.titulo-texto'),
            'tipo': tipo,
            'texto': text,
            'data': get_simples('.data'),
            'bibliografia': get_simples('.biblio'),
        }

        self.num_processados += 1
        self.logger.info(
            f'Item #{dados["id"]} processado ({self.num_processados} processados no total)')

        yield dados
