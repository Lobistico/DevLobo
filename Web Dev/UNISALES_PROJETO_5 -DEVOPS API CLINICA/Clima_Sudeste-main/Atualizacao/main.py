from funcoes.funcoes_clima import *

root = get_url('http://servicos.cptec.inpe.br/XML/capitais/condicoesAtuais.xml')  # ARQUIVO XML DA NUVEM

df = convertendo(root)  # CONVERTE XML IN DATAFRAME

atualiza_base_dados(root)  # ATUALIZA O BANCO DE DADOS
salvar_imagem(df) # SALVA A TABELA EM IMAGEM
visualiza_grafico(df, 'codigo', 'temperatura') # VISUALIZA GRÁFICO

base_dado_to_csv() # SALVA BASE DE DADOS EM CSV
