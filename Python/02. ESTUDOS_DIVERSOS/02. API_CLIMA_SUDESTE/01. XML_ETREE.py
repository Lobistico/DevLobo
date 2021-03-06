# -*- coding: utf-8 -*-
"""Estudo_xml_etree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Q3Gd5nprg3rzGHoX_veSbe2JeeeEhsO
"""

# OBRIGATÓRIO
import xml.etree.ElementTree as ET
import requests

# IMPORTA ARQUIVO XML
url = "http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml"
header = { 'Accept': 'application/xml' }
r = requests.get(url, headers=header)

tree =  ET.ElementTree(ET.fromstring(r.content))	
root = tree.getroot()
# LISTA DAS ESTAÇÕES DO ESTADO DO ES
códigos = ['SBRJ','SBSP','SBVT', 'SBCF']

# TESTE DE VERIFICAÇÃO UM
teste ={}
for i  in range(0, 26):
  if root[i][0].text in códigos:
    teste[root[i][0].text] = root[i][3].text
    print(f' Na estação {root[i][0].text} está fazendo {root[i][3].text} graus')

# IMPRIME A TABELA PANDAS.
import pandas as pd
pd.Series(teste)

# print(root[0][0].text) 

#VISUALIZA_RAIZ
#print(root.attrib)

# #ESTUDO_VISUALIZAR_METAR ___TESTE DE INTEGRAÇÃO
# for child in root:
#   for codigo in child:
#     #for valor in codigo:
#       print(codigo.text)
#     #print(codigo.tag, codigo.attrib)
#     # print(child.tag, child.attrib)


# # VERIFICAÇÃO LÓGICA --- TESTE DE VERIFICAÇÃO
# for child in root.findall("metar"):
#     for title in child.findall("codigo"):
#       if title.text in códigos:        
#         print(title.text)


# print(root[0][0].text)  acessa o primeiro item do xml