# Webscraping da agenda do Lula com a biblioteca Scrapy (páginas estáticas)

# importar bibliotecas
import scrapy
import pandas as pd
import os
import datetime as dt
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', 
                    datefmt='%d-%b-%y %H:%M:%S')

# Definir o caminho da pasta "dadosdaagenda"
folder_path = "dadosdaagenda"

# Criar a pasta "output" 
output_path = os.path.join(folder_path, "output")
if not os.path.exists(output_path):
    os.mkdir(output_path)

class AgendaSpider(scrapy.Spider):
    name = "agenda"
    
    # Automatizar downloads de 01-01-2023 até o dia de hoje
          
    start_date = dt.date(2023, 1, 1) 
    end_date = dt.date.today()  
    delta = dt.timedelta(days = 1)
    days = []  
    
    
    while start_date <= end_date:
        days.append(start_date.strftime('%Y-%m-%d'))
        start_date += delta

            
    def start_requests(self):
        for day in self.days:
             url = f'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica-lula/agenda-do-presidente-da-republica/{day}'
             yield scrapy.Request(url=url, callback=self.parse)   
                   
    # raspar os dados  
    def parse(self, response):
                        
        autoridade = response.css('h1.documentFirstHeading::text').extract_first()       
                        
        titulo = response.css('h2.compromisso-titulo::text').extract()
            
        local = response.css('div.compromisso-local::text').extract()
            
        horario = response.css('time.compromisso-inicio::text').extract()
            
        # print(f'Título: {titulo} - Local: {local} - Horário: {horario}- Autoridade: {autoridade}')
            
        # criar um dataframe com os dados 
        df = pd.DataFrame({'titulo':titulo, 'local':local, 'horario':horario})
            
        # inserir coluna com a data    
        df['data'] = response.url.split('/')[-1]
        
        # criar coluna com o cargo da autoridade
        df['autoridade'] = autoridade
            
        # criar o df que vai armazenar os dados
        df_final = pd.DataFrame(columns=['titulo', 'local', 'horario', 'data', 'autoridade'])    
                     
        df_final = pd.concat([df_final, df], ignore_index=True)
                                
        #print(df_final)
        
        # exportar no formato csv    
        df_final.to_csv('dadosdaagenda/output/compromissos.csv', sep = ';', mode='a', index=False, header=not os.path.exists('dadosdaagenda/output/compromissos.csv'))
                