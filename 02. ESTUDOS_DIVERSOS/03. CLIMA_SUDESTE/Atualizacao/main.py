import matplotlib
import xml.etree.ElementTree as xeET
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import dataframe_image as dfi

# IMPORTA ARQUIVO XML
url = "http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml"
header = {'Accept': 'application/xml'}
r = requests.get(url, headers=header)

tree = xeET.ElementTree(xeET.fromstring(r.content))
root = tree.getroot()

# LISTA DAS ESTAÇÕES DOS ESTADOS
codigos = ['SBRJ', 'SBSP', 'SBVT', 'SBCF']
cidades = ['Rio de Janeiro', 'São Paulo', 'Vitória', 'Belo Horizonte']
dc_cid_cod = {}

# SALVA AS ESTAÇÕES
for k, j in zip(codigos, cidades):
    dc_cid_cod[k] = j
    # print(j)

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS previsao_tempo ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'codigo TEXT,'
               'atualizacao TEXT,'
               'temperatura INTEGER,'
               'ar_umido INTEGER,'
               'a_tempo TEXT'
               ')')
teste = {}  # Salva um dicionário teste com temperatura e estação.
predominio = []  # Salva o predominio do momento.
errado_predominio = ['PredomÃ\xadnio de Sol', 'Chuvas periÃ³dicas']  # predominio errado

for i in range(0, 26):
    if root[i][0].text in codigos:
        teste[root[i][0].text] = root[i][3].text
        
        if root[i][5].text == errado_predominio[0]:
            predominio.append(root[i][5].text)
            predominio_certo = 'Sol Predominante'
            cursor.execute(
                'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, ar_umido, a_tempo) VALUES (?, ?, ?, ?,?)'
                , (dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, root[i][6].text, predominio_certo))
        elif root[i][5].text == errado_predominio[1]:
            predominio.append(root[i][5].text)
            predominio_certo = 'Chuvas Casuais'
            cursor.execute(
                'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, ar_umido, a_tempo) VALUES (?, ?, ?, ?,?)'
                , (dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, root[i][6].text, predominio_certo))
        else:
            predominio.append(root[i][5].text)
            cursor.execute(
                'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, ar_umido, a_tempo) VALUES (?, ?, ?,?,?)'
                , (dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, root[i][6].text, root[i][5].text))
conexao.commit()
cursor.close()
conexao.close()

# CORRIGE ACENTO DO PREDOMINIO
for x in range(0, len(predominio)):
    predominio[x] = predominio[x].replace('Ã³', 'ó')
    predominio[x] = predominio[x].replace('Ã\xad', 'í')

# CRIA O TABELA COM A TEMPERATURA
estacao = list(teste)
temperatura = list(teste.values())
d = {'Estacao': estacao, 'Temperatura': temperatura, 'Predominio': predominio}
df = pd.DataFrame(data=d)

df['Temperatura'] = pd.to_numeric(df['Temperatura'])  # Converte para Integer
print(df)

# opcoes_sim = ['sim', 'yes', 's']
# show_grafico = input('Digite "sim" para visualizar o gráfico?\n').lower()
# VISUALIZA O GRÁFICO
grafico = df.groupby(df['Estacao'])['Temperatura'].sum().plot.barh(title='Temperatura', color='red',
                                                                       figsize=(20, 5))
plt.savefig('../paginas/static/paginas/img/gráfico.jpg')
# matplotlib.pyplot.show() -- mostra o gráfico


# SALVANDO UMA IMAGEM
df_styled = df.style.background_gradient()
dfi.export(df_styled, "../paginas/static/paginas/img/registro.jpg")
