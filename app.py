import sqlite3

conn = sqlite3.connect("CADASTRO_ITENS.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS categorias (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL UNIQUE)")
cursor.execute("CREATE TABLE IF NOT EXISTS itens (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, quantidade INTEGER NOT NULL, preco REAL NOT NULL, categoria_id INTEGER, FOREIGN KEY (categoria_id) REFERENCES categorias(id))")

cursor.execute("INSERT INTO categorias (nome) VALUES ('Mercado')")
cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Arroz', 2, 15.99, 1)")

cursor.execute("SELECT * FROM categorias")
print(cursor.fetchall())

cursor.execute("SELECT * FROM itens")
print(cursor.fetchall())

cursor.execute("UPDATE itens SET preco = 17.50 WHERE id = 1")

cursor.execute("SELECT * FROM itens")
print(cursor.fetchall())

cursor.execute("DELETE FROM itens WHERE id = 1")

cursor.execute("SELECT * FROM itens")
print(cursor.fetchall())

conn.commit()
conn.close()
