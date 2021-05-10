from unicodedata import normalize
from nltk.tokenize import word_tokenize
import nltk
import re


class TextUtil:
    """
    Classe com métodos para tratamento de texto
    """

    def RemoverCaracteresEspeciais(self, text):
        """
        Método para remover caracteres especiais do texto
        """
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

    def RemoverPontuacoes(self,text):
        """
                Método para remover pontuações do texto
        """

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~“…”’'''
        for x in punctuations:
            text = text.replace(x, " ")
        return text

    def RemoverPalavrasSemSentido(self,text):
        """
                Método para remover palavras sem sentido do texto
        """

        # seleciona apenas letras e coloca todas em minúsculo
        letras_min = re.findall(r'\b[A-zÀ-úü]+\b', text.lower())

        stopwords = nltk.corpus.stopwords.words('portuguese')
        stop = set(stopwords)
        sem_sentido = ['de', 'nao','r', 'e', 'do', 'o', 'meu', 'a', 'que', 'no', 'da', 'consigo', 'para', 'com', 'me',
                       'mas', 'uma', 'minha', 'foi', 'tenho', 'na', 'um', 'em', 'mais', 'por', 'fiz', 'esta',
                       'pelo', 'esta', 'estou', 'ja', 'eu', 'essa', 'compartilhe', 'pois', 'se', 'isso', 'ate', 'esse',
                       'quero', 'ao', 'mesmo', 'sendo', 'os', 'pra', 'as', 'porem', 'nada',
                       'ou', 'hoje', 'nem', 'fazer', 'ainda', 'dia', 'como', 'fui', 'dias', 'sem', 'recebi', 'sendo',
                       'tem', 'agora', 'solicitei', 'gostaria', 'so', 'porque', 'mes', 'aqui',
                       'eles', 'vou', 'nunca', 'ter', 'era', 'ser', 'quando', 'entao', 'muito', 'assim', 'preciso',
                       'tinha', 'magazine', 'meses', 'estava', 'sempre', 'luiza', 'havia', 'estao', 'sou',
                       'tudo', 'vou', 'boa', 'disse', 'seja', 'novamente', 'r', 'nome', 'vez', 'entrei', 'tambem',
                       'voces', 'desde', 'empresa', 'recebendo', '2', 'cliente', 'consta', 'pessoa', 'via', 'erro', 'falta',
                       'codigo', 'recebendo', 'ainda', 'reclame', 'editado', 'lendico', 'luizacred']
        stop.update(sem_sentido)

        sem_stopwords = [w for w in letras_min if w not in stop]

        # juntando os tokens novamente em formato de texto
        texto_limpo = " ".join(sem_stopwords)

        return texto_limpo


    def Lemmatizador(self,text):

        """
            Método que utiliza o lemmatizador da bibliotexa nltk no texto
        """

        tokens = word_tokenize(text)
        wnl = nltk.WordNetLemmatizer()

        tokens = [wnl.lemmatize(t) for t in tokens]
        tokens = str(tokens)
        return tokens

    def Tratamento_personalizado(self,text):

        """
            Método que faz uma normalização de palavras similares
        """

        words = {
            'aplicativo ':      'app ',
            'abusivo ':         'abusiva ',
            'abusivas ':        'abusiva ',
            'abusivos ':        'abusiva ',
            'acesso ':          'acessar ',
            'antecipada ':      'antecipar ',
            'antecipar ':       'antecipar ',
            'antecipei ':       'antecipar ',
            'antecipados ':     'antecipar ',
            'antecipadas ':     'antecipar ',
            'antecipadamente ': 'antecipar ',
            'antecipado ':      'antecipar ',
            'antecipacao ':     'antecipar ',
            'baixar ':          'baixa ',
            'baixado ':         'baixa ',
            'baixada ':         'baixa ',
            'baixadas ':        'baixa ',
            'baixaram ':        'baixa ',
            'baixam ':          'baixa ',
            'baixados ':        'baixa ',
            'baixaam ':         'baixa ',
            'baixas ':          'baixa ',
            'boletos ':         'boleto',
            'bloqueado ':       'bloqueio ',
            'cancelamento ':    'cancelar ',
            'cancelado ':       'cancelar ',
            'cancelei ':        'cancelar ',
            'cancelamentoo ':   'cancelar ',
            'chegou':           'chegar ',
            'chega':            'chegar ',
            'car seguros ':     'seguro ',
            'car* seguros ':    'seguro ',
            'car seguro ':      'seguro ',
            'carseguro ':       'seguro ',
            'cadastrado ':      'cadastro ',
            'cobrancas ':       'cobranca ',
            'contratos ':       'contrato ',
            'cobrando ':        'cobranca ',
            'cobrado ':         'cobranca ',
            'dividas ':         'divida ',
            'desbloqueio ':      'desbloquear ',
            'emprestimos ':     'emprestimo ',
            'empresta ':        'emprestimo ',
            'indevidamente ':   'indevida ',
            'indevidas ':       'indevida ',
            'indevidos ':       'indevida ',
            'indevido ':        'indevida ',
            'parcelei ': 'parcela ',
            'parcelas ':        'parcela ',
            'parcelado ':       'parcela ',
            'pagamentos ':      'pagamento ',
            'paguei ':          'pagamento ',
            ' paga ':            'pagamento ',
            ' pagar ':           'pagamento ',
            ' pago ':            'pagamento ',
            'pagamentomento ':  'pagamento ',
            'propagamentonda ': 'pagamento ',
            'problemas ':       'problema ',
            'quitacao ':        'quitar ',
            'quitado ':         'quitar ',
            'quitando ':        'quitar ',
            'quitadas ':        'quitar ',
            'servico ':         'servicos ',
            'seguros ':         'seguro ',
            'spc ':             'serasa',
            'telefone ':        'atendimento',
            'token ':           'itoken ',
            'enrolar ':         'demora ',
            'enrolacao ':       'demora ',
            'mensagens ':       'mensagem ',
            'limiti ':          'limite ',
            'atende ':          'atendimento',
            'cadastro    positivo': 'serasa ',
            'sms':              'mensagem ',
            'sm':               'mensagem ',
            'ligação':          'ligações',
            'ligando':          'ligações',
            'faturas':          'fatura',
            'atentende ':        'atendimento ',
            ' mail ':           'email',
            ' boletos ':        'boleto',
            'documentos':       'documento',
            'plataforma':       'site',
            'sistema':          'site',
            'hackers':          'hacker',
            'hackearam':        'hacker',
        }

        for word, initial in words.items():
            text = text.replace(word, initial)

        return text


