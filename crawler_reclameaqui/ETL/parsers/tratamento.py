from database.database import db
import datetime
from parsers.parsing import *
from collections import Counter


def insert_values(cont):
    cont += 1
    if cont/500 == 1.0:
        db.session.commit()
        cont = 1
    return cont


def null_values(dicionario):
    for x, y in dicionario.items():
        if str(y) in ['', '{}']:
            dicionario[x] = None

    return dicionario


def tratamento_json(x, titulo):

    split = x

    if titulo == 'titulo':
        parse = split[0].strip()
    elif titulo == 'descricao':
        parse = split[1].replace('Compartilhe essa reclamação:', '').strip()[:5000]

    tratamento = TextUtil()
    json = tratamento.RemoverPalavrasSemSentido(parse)
    json = tratamento.Lemmatizador(json)
    json = tratamento.RemoverCaracteresEspeciais(json)
    json = tratamento.RemoverPontuacoes(json)
    json = tratamento.Tratamento_personalizado(json)
    json = dict(Counter(json.lower().split()))

    return json


def classe_json(x, titulo):

    classes = {
        'baixa': 0,
        'parcela': 0,
        'boleto': 0,
        'email': 0,
        'site': 0,
        'acessar': 0,
        'serasa': 0,
        'finalizar': 0,
        'app': 0,
        'dado': 0,
        'cadastro': 0,
        'instabilidade': 0,
        'contrato': 0,
        'desbloquear': 0,
        'quitar': 0
    }

    split = x

    if titulo == 'titulo':
        parse = split[0].strip()
    elif titulo == 'descricao':
        parse = split[1].replace('Compartilhe essa reclamação:', '').strip()[:5000]
    elif titulo == 'geral':
        parse = split[0].strip() + ' ' + split[1].replace('Compartilhe essa reclamação:', '').strip()[:5000]

    tratamento = TextUtil()
    json = tratamento.RemoverPalavrasSemSentido(parse)
    json = tratamento.Lemmatizador(json)
    json = tratamento.RemoverCaracteresEspeciais(json)
    json = tratamento.RemoverPontuacoes(json)

    json = tratamento.Tratamento_personalizado(json)
    json = dict(Counter(json.lower().split()))

    for x in json.keys():
        if x in classes.keys():
            classes[x] = 1

    for key, value in dict(classes).items():
        if value != 1:
            del classes[key]
    return classes

def tratamento_dados(x):


    split = x.split(';')

    titulo_json = tratamento_json(split, 'titulo')
    descricao_json = tratamento_json(split, 'descricao')
    classes_titulo = classe_json(split, 'titulo')
    classes_descricao = classe_json(split, 'descricao')
    classes = classe_json(split, 'geral')
    dados = {
        'titulo': split[0].strip(),
        'descricao': split[1].replace('Compartilhe essa reclamação:','').strip()[:5000],
        'cidade': split[2][:split[2].find('ID')-5].strip(),
        'estado': split[2][split[2].find('ID')-3:split[2].find('ID:')].strip(),
        'id': int(split[2][split[2].find('ID:')+3:split[2].find('/')-2].strip()),
        'data': datetime.datetime.strptime(split[2][split[2].find('/')-2:split[2].find('às')].strip().replace('/', '-'),"%d-%m-%y").strftime("%Y-%m-%d").strip(),
        'hora': split[2][split[2].find('às')+2:].replace('h', ':').replace("denunciar","").strip(),
        'link': split[3].replace('\n', '').strip(),
        'updated_at': datetime.datetime.now(),
        'dominio': split[4].replace('\n', '').strip(),
        'titulo_json': titulo_json,
        'descricao_json': descricao_json,
        'classes_titulo': classes_titulo,
        'classes_descricao': classes_descricao,
        'classes': classes,
    }

    return dados