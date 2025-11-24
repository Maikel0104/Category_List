import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO categorias (nome) VALUES ('Açougue')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Limpeza')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Hortifruti')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Perecíveis')")
cursor.execute("INSERT INTO categorias (nome) VALUES ('Higiene')")
conn.commit()

cursor.execute("SELECT * FROM categorias")
print(cursor.fetchall())

conn.close()
