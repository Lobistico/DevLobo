import sqlite3
import pandas as pd

# RECUPERAÇÃO DE DADOS - SALVOS EM CSV
conect = sqlite3.connect('basededados.db')

dados_recuperados = pd.read_sql_query("SELECT * FROM previsao_tempo", conect)
df = pd.DataFrame(dados_recuperados)
df.to_csv(sep=',', index=False, path_or_buf='dad.csv')

dff = pd.read_csv(filepath_or_buffer=r"C:\Users\eduar\Desktop\Py-Projects\02.ESTUDOS_DIVERSOS\03.CLIMA_SUDESTE\dad.csv",
                  sep=',')
# dff = dff['atualizacao'] = pd.to_datetime(dff['atualizacao'])
print(dff)
