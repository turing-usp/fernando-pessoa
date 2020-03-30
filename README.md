# Classificador de Heterônimos do Fernando Pessoa

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GrupoTuringCodes/fernando-pessoa/master)

## Pré-requisitos

Esse projeto foi desenvolvido utilizado Python 3 e Jupyter notebooks. Ele pode ser visualizado online em um [binder](https://mybinder.org/v2/gh/GrupoTuringCodes/fernando-pessoa/master).

Alternativemente, as dependências desse projeto estão listadas em [requirements.txt](requirements.txt). Para instalá-las, utilize o comando:

```bash
pip install -r requirements.txt
```

## Guia de Uso

### Extração de Dados

Os dados foram extraídos do site [arquivopessoa.net](http://arquivopessoa.net/) utilizando [scrapy](https://scrapy.org/) e estão disponíveis no arquivo _[fernando_pessoa.csv](fernando_pessoa.csv)_. As colunas do dataset estão exemplificadas abaixo:

|   id | autor           | titulo                                                     | tipo   | texto                                                         | data      | bibliografia                                                   |
|-----:|:----------------|:-----------------------------------------------------------|:-------|:--------------------------------------------------------------|:----------|:---------------------------------------------------------------|
|    4 | Ricardo Reis    | Diana através dos ramos                                    | poesia | Diana através dos ramos<br/>Espreita a vinda de Endymion...   | 16-6-1914 | Poemas de Ricardo Reis. Fernando Pessoa. (Edição Crítica de... |
|    5 | Fernando Pessoa | A REFORMA DO CALENDÁRIO E AS SUAS CONSEQUÊNCIAS COMERCIAIS | prosa  | A REFORMA DO CALENDÁRIO E AS SUAS CONSEQUÊNCIAS COMERCIAIS... | 10-3-1933 | Páginas de Pensamento Político. Vol II. Fernando Pessoa...     |

Para rodar o scraper, basta executar:

```bash
scrapy crawl ArquivoPessoa -o fernando_pessoa.csv
```

## Créditos

Esse projeto depende das seguintes bibliotecas:

- [NumPy](https://www.numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [seaborn](https://seaborn.pydata.org/)
- [scikit-learn](https://scikit-learn.org)
- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)
- [scrapy](https://scrapy.org/)
- [html2text](https://pypi.org/project/html2text/)

## Autores

Desenvolvido pela área de PLN (processamento de linguagem natural) do [Grupo Turing](https://github.com/GrupoTuringCodes):

- [Fernando Matsumoto](https://github.com/fernandokm)
- [Iago Nunes](https://github.com/juliapocciotti)
- [Igor de Camargo](https://github.com/IgorCSC)
- [Júlia Pocciotti](https://github.com/juliapocciotti)
- [Lucas Sepeda](https://github.com/likury)

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
