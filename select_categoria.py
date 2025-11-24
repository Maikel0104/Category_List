import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

categoria = "Mercearia"

cursor.execute("SELECT id FROM categorias WHERE nome = ?", (categoria,))
cat = cursor.fetchone()

if cat:
    cursor.execute("SELECT id, nome, quantidade, preco FROM itens WHERE categoria_id = ?", (cat[0],))
    print(cursor.fetchall())
else:
    print("Categoria não encontrada.")

conn.close()
