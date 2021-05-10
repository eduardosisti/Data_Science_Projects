import pandas as pd
from parsers.banco_de_dados import *
from models.Reclamacoes import *
from parsers.tratamento import *
from database.database import db
from models.base import *
import os


def insert_carga():
    conexao = banco_de_dados()
    consulta = conexao.consultar('select reclamacoes.link from reclamacoes')
    if consulta is None or len(consulta) == 0:
        consulta = []
    else:
        consulta = list(consulta[0])
    conexao.fechar()

    cont = 0
    with open(os.getenv('PROCESS_PATH'), 'r', encoding='utf-8') as f:
        first_line = f.readline()
        for x in f:
            split = tratamento_dados(x)

            if split['link'] in consulta:
                continue
            split = null_values(split)
            Reclamacoes.create_on_conflict([Reclamacoes.link], ignore=False, update=True, **split)
            cont = insert_values(cont)

        try:
            db.session.commit()
        except:
            pass