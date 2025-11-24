import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

cursor.execute("UPDATE itens SET preco = 17.50 WHERE id = 1")
conn.commit()

cursor.execute("SELECT * FROM itens WHERE id = 1")
print(cursor.fetchone())

conn.close()
