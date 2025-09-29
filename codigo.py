import sqlite3

# Criar uma conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("biblioteca.db")

# Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

# Criar uma tabela 

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL, 
    autor TEXT NOT NULL,
    ano INTENGER,
    disponivel TEXT DEFAULT "sim",
    )
""")
