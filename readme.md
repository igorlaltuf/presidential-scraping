# Webscraping da agenda presidencial com a biblioteca Scrapy

Este repositório é um projeto pessoal em Python que tem como objetivo criar um arquivo csv com os dados da agenda presidencial desde janeiro de 2023 e disponibilizada em: https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica-lula/agenda-do-presidente-da-republica/2023-03-29.


## Requisitos
Git 

Python >= 3.10.2

Virtualenv >= 20.13.0

## Instalação

1 - Baixe o repositório
```
git clone https://github.com/igorlaltuf/presidential-scraping.git
$ cd presidential-scraping
```


2 - Crie um ambiente virtual e o ative
```
python -m venv env
env/Scripts/Activate
```


3 - No ambiente, instale os pacotes
```
pip install -r requirements.txt
```


## Forma de usar

1) Abrir a pasta "presidential-scraping" e executar o comando "env/Scripts/Activate" para carregar o ambiente (caso ainda não tenha feito no passo anterior). 

2) Execute o comando "scrapy crawl agenda" para iniciar o web scraping.

3) Execute o comando "deactivate" para sair do ambiente.

Agora basta acessar o arquivo compromissos.csv que está dentro da pasta output.
