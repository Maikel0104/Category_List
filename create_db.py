import sqlite3

conn = sqlite3.connect("Cadastra_Produtos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 1,
    preco REAL NOT NULL DEFAULT 0,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
""")

conn.commit()
conn.close()

print("DB e tabelas criadas.")
