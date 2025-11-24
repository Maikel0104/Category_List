import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM itens WHERE id = 1")
conn.commit()

cursor.execute("SELECT * FROM itens")
print(cursor.fetchall())

conn.close()
