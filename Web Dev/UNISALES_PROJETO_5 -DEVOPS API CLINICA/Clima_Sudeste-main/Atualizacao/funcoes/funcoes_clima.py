import xml.etree.ElementTree as xeE
# import sqlite3
import requests
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import dataframe_image as dfi


def get_url(link):
	"""
	:param link: STR - Link do XML
	:return: raiz do xml que dever ser associado a uma variavel
	"""
	url = link
	header = {'Accept': 'application/xml'}
	r = requests.get(url, headers=header)
	tree = xeE.ElementTree(xeE.fromstring(r.content))
	return tree.getroot()


def atualiza_base_dados(root):
	"""
	:param root: recebe como parametro a variavel raiz do arquivo xml associada com o get_url
	:return: os arquivos são salvos no banco de dados
	"""
	
	# INICO BASE DADOS
	conexao = sqlite3.connect('basededados.db')
	cursor = conexao.cursor()
	
	cursor.execute('CREATE TABLE IF NOT EXISTS previsao_tempo ('
	               'codigo TEXT,'
	               'atualizacao DATETIME,'
	               'temperatura INTEGER,'
	               'tempo_desc TEXT'
	               ')')
	
	for i in range(0, len(list(root))):
		if root[i][0].text in codigos:
			if root[i][5].text == errado_predominio[0]:
				predominio_certo = 'Sol Predominante'
				cursor.execute(
					'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, tempo_desc) '
					'VALUES (?, ?, ?, ?)',
					(dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, predominio_certo))
			elif root[i][5].text == errado_predominio[1]:
				predominio_certo = 'Chuvas Casuais'
				cursor.execute(
					'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, tempo_desc) '
					'VALUES (?, ?, ?, ?)',
					(dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, predominio_certo))
			else:
				cursor.execute(
					'INSERT INTO previsao_tempo (codigo, atualizacao, temperatura, tempo_desc)'
					'VALUES (?, ?, ?, ?)',
					(dc_cid_cod[root[i][0].text], root[i][1].text, root[i][3].text, root[i][5].text))
	
	conexao.commit()
	cursor.close()
	conexao.close()


def convertendo(root):
	"""
	:param root:  recebe como parametro a variavél raiz do arquivo xml da api clima associada com o get_url
	:return: dados filtrados pelas cidades do sudeste brasileiro.
	"""
	cols = ['codigo', 'atualizacao', 'temperatura', 'tempo_desc']
	rows = []
	for i in root:
		codigo = i.find('codigo').text
		atualizacao = i.find('atualizacao').text
		temperatura = i.find('temperatura').text
		tempo_desc = i.find('tempo_desc').text
		
		rows.append(
			{'codigo': codigo, 'atualizacao': atualizacao, 'temperatura': temperatura, 'tempo_desc': tempo_desc})
	
	new = {"PredomÃ\xadnio de Sol": "Sol Predominante", 'Chuvas periÃ³dicas': 'Chuvas Casuais'}
	new.update(dc_cid_cod)
	df = pd.DataFrame(rows, columns=cols)
	df = df.replace(new)
	df['temperatura'] = pd.to_numeric(df['temperatura'])
	filtered_df = (df.loc[df['codigo'].isin(cidades)])
	return filtered_df


def visualiza_grafico(variavel_tabela, coluna1, coluna2):
	"""
	:param variavel_tabela: variavel df gerada do arquivo xml
	:param coluna1: a coluna TEXT
	:param coluna2: a coluna com valor INTEGER
	:return: salva figura para o front-end
	"""
	grafico = variavel_tabela.groupby(variavel_tabela[coluna1])[coluna2].sum().plot.barh(
		title='Temperatura', color='red', figsize=(20, 5))
	plt.savefig('../front/static/img/gráfico.jpg') #quando começa o
	#matplotlib.pyplot.show()


def salvar_imagem(variavel_tabela):
	"""
	:param variavel_tabela:variavel df gerada do arquivo xml
	:return: imagem da tabela
	"""
	variavel_tabela = variavel_tabela.rename(columns={'codigo':'Cidade','atualizacao':'Registro',
	                                                  'temperatura':'Temperatura (ºC)', 'tempo_desc':'Predominância'})
	
	df_styled = variavel_tabela.style.background_gradient()
	dfi.export(df_styled, '../front/static/img/registro.jpg')  # STRING É O ENDEREÇO "../front/static/img/registro.jpg"


def base_dado_to_csv():
	conect = sqlite3.connect('basededados.db')
	dados_recuperados = pd.read_sql_query("SELECT * FROM previsao_tempo", conect)
	df = pd.DataFrame(dados_recuperados)
	df.to_csv(sep=',', index=False, path_or_buf='base_dados.csv')


# LISTA DAS ESTAÇÕES DOS ESTADOS
codigos = ['SBRJ', 'SBSP', 'SBVT', 'SBCF']
cidades = ['Rio de Janeiro', 'São Paulo', 'Vitória', 'Belo Horizonte']
dc_cid_cod = {}

# SALVA AS ESTAÇÕES
for k, j in zip(codigos, cidades):
	dc_cid_cod[k] = j

# Para corrigir predominio
errado_predominio = ['PredomÃ\xadnio de Sol', 'Chuvas periÃ³dicas']