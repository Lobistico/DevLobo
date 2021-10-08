import matplotlib
import xml.etree.ElementTree as ET
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# IMPORTA ARQUIVO XML
url = "http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml"
header = { 'Accept': 'application/xml' }
r = requests.get(url, headers=header)

tree =  ET.ElementTree(ET.fromstring(r.content))
root = tree.getroot()

# LISTA DAS ESTAÇÕES DOS ESTADOS
codigos = ['SBRJ','SBSP','SBVT', 'SBCF']
cidades = ['Rio de Janeiro', 'São Paulo', 'Vitória', 'Belo Horizonte']
dc_cid_cod ={}

# SALVA AS ESTAÇÕES
for k,j in zip(codigos, cidades):
  dc_cid_cod[k] = j
  #print(j)

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
teste ={} # Salva um dicionário teste com temperatura e estação.
predominio=[] # Salva o predominio do momento.

for i in range(0, 26):
  if root[i][0].text in codigos:
    teste[root[i][0].text] = root[i][3].text
    predominio.append(root[i][5].text)
    cursor.execute('INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, ar_umido, a_tempo) VALUES (?, ?, ?, ?,'
                   ' ?)', (dc_cid_cod[root[i][0].text],root[i][1].text,root[i][3].text,root[i][6].text,root[i][5].text))
conexao.commit()
cursor.close()
conexao.close()

# CORRIGE ACENTO DO PREDOMINIO
for x in range(0, len(predominio)):
    predominio[x] = predominio[x].replace('Ã\xad', 'í')
    predominio[x] = predominio[x].replace('Ã³', 'ó')

# CRIA O TABELA COM A TEMPERATURA
estacao = list(teste)
temperatura = list(teste.values())
d = {'Estacao': estacao, 'Temperatura': temperatura, 'Predominio': predominio}
df = pd.DataFrame(data=d)

df['Temperatura'] = pd.to_numeric(df['Temperatura']) # Converte para Integer
print(df)

opcoes_sim = ['sim','yes','s']
show_grafico = input('Digite "sim" para visualizar o gráfico?\n').lower()
# VISUALIZA O GRÁFICO
if show_grafico in opcoes_sim:
    grafico = df.groupby(df['Estacao'])['Temperatura'].sum().plot.barh(title= 'Temperatura', color ='red',
                                                                           figsize=(20,5));
    matplotlib.pyplot.show()

# RECUPERAÇÃO DE DADOS - SALVOS EM CSV
conect = sqlite3.connect('basededados.db')

dados_recuperados = pd.read_sql_query("SELECT * FROM previsao_tempo", conect)
dados_recuperados.to_csv('dados.csv',index=False)

# IMPORTA O CSV
x = 'dados.csv'
dff = pd.read_csv(x, encoding= 'unicode_escape', error_bad_lines=False,sep=',')
dff['atualizacao'] = pd.to_datetime(dff['atualizacao'])
matplotlib.pyplot.show()
