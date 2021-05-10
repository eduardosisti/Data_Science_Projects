from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import csv

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

if not os.path.exists(f'/{os.getenv("VOLUME_NAME")}/controler.csv'):
    with open(f'/{os.getenv("VOLUME_NAME")}/controler.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Link"])

if not os.path.exists(f'/{os.getenv("VOLUME_NAME")}/reclamacoes.csv'):
    with open(f'/{os.getenv("VOLUME_NAME")}/reclamacoes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Titulo", "Descricao", "Cidade_data", "Link", "Dominio"])


class ReclameAqui:
    base_url = "https://www.reclameaqui.com.br/empresa/"

    def __init__(self, empresa):
        self.driver = webdriver.Chrome('/Webscraping/chromedriver', options=chrome_options)
        self.empresa = empresa

    def extrair_informacoes(self, n_paginas):
        url = self.base_url + self.empresa + "/lista-reclamacoes/?pagina="

        controler = pd.read_csv(f'/{os.getenv("VOLUME_NAME")}/controler.csv', encoding="ISO-8859-1")

        for i in range(1, n_paginas + 1):
            self.reclamacoes, self.titulos, self.links = [], [], []
            self.driver.get(url + str(i))
            sleep(3)

            html = bs(self.driver.page_source, "html.parser")

            reclamacoes_html = html.find_all("p", {"class": "text-detail"})
            reclamacoes_na_pagina = [reclamacao.text.split("|") for reclamacao in reclamacoes_html]
            self.reclamacoes.extend(reclamacoes_na_pagina)

            titulos_e_links = html.find_all(
                "a", {"class": "link-complain-id-complains"}
            )
            self.titulos.extend([titulo.text.strip() for titulo in titulos_e_links])
            self.links.extend([link.get("href") for link in titulos_e_links])

            urls = [self.base_url + link[1:] for link in self.links]
            self.descricoes, self.data_hora, self.url_code, self.titulo, self.dominio = [], [], [], [], []

            for url_code in urls:
                if url_code in list(controler['Link']):
                    continue
                self.driver.get(url_code)
                sleep(3)
                try:
                    html = bs(self.driver.page_source, "html.parser")
                    titulo = html.find('h1', {"class": "ng-binding"}).text.strip().replace('"', "'").replace(";", ",")
                    descricao = html.find("div", {"class": "complain-body"}).text.strip().replace('"', "'").replace(";", ",")
                    data_hora = html.find("ul", {"class": "local-date list-inline"}).text.strip()
                    dominio = self.empresa
                    self.titulo.append(titulo)
                    self.descricoes.append(descricao)
                    self.data_hora.append(data_hora)
                    self.url_code.append(url_code)
                    self.dominio.append(dominio)
                except:
                    continue

            if len(self.descricoes) > 0:
                dados = {'Titulo': self.titulo, 'Descricao': self.descricoes, 'Cidade_data': self.data_hora,
                         'Link': self.url_code, 'Dominio': self.dominio}
                df = pd.DataFrame(data=dados)
                df.to_csv(f'/{os.getenv("VOLUME_NAME")}/reclamacoes.csv', mode='a', sep=';', header=False, index=False)
                df['Link'].to_csv(f'/{os.getenv("VOLUME_NAME")}/controler.csv', mode='a', header=False, index=False)


info = ReclameAqui(os.getenv("RECLAME_AQUI_EMPRESA"))
info.extrair_informacoes(100)
