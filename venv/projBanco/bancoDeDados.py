import sqlite3
con = sqlite3.connect('baseDeDados.db') #criando base
cur = con.cursor() #conectando cursor
#sintaxe do sql
sql = """
    CREATE TABLE contas_bancarias (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        numeroConta TEXT NOT NULL UNIQUE,
        nome TEXT NOT NULL,
        saldo FLOAT NOT NULL DEFAULT 0.0,
        status TEXT NOT NULL DEFAULT 'ativa'
    )
"""
cur.execute(sql)
con.commit() #executar os comandos na nossa base
con.close()