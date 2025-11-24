import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Costela_Minga', 10, 23.99, 1)")
cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Detergente', 3, 2.50, 2)")
cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Alface', 3, 1.99, 3)")
cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Arroz_5kg', 50, 15.50, 4)")
cursor.execute("INSERT INTO itens (nome, quantidade, preco, categoria_id) VALUES ('Desodorante_Avanço', 10, 5.80, 5)")

conn.commit()

cursor.execute("SELECT * FROM itens")
print(cursor.fetchall())

conn.close()
