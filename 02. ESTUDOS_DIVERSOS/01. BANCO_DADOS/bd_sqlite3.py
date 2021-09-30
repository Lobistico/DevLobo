import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("EDUARDO RODRIGUES", 60)')
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()