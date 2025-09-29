import sqlite3
from funcoes import cadastrar_livros, listar_livros

# Criar uma conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("biblioteca.db")

# Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

# Criar uma tabela 

cursor.execute("""
CREATE TABLE IF NOT EXISTS biblioteca (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL, 
    autor TEXT NOT NULL,
    ano TEXT NOT NULL,
    disponivel TEXT
    )
""")

titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
ano = input("Digite o ano do livro: ")
disponivel = input("O livro está disponível? (sim/não): ")

cadastrar_livros(titulo, autor, ano, disponivel)

print(listar_livros())