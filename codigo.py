import sqlite3
from funcoes import cadastrar_livros, listar_livros, atualizar_livros, deletar_livro

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

"""titulo = input("Digite o título do livro: ").strip().lower()
autor = input("Digite o autor do livro: ").strip().lower()
ano = input("Digite o ano do livro: ").strip().lower()
disponivel = input("O livro está disponível? (sim/não): ").strip().lower()

cadastrar_livros(titulo, autor, ano, disponivel)

print(listar_livros())"""

"""id = int(input("Digite o ID do livro que deseja atualizar: "))

while True:
    print("\nEscolha o que deseja atualizar:")
    print("1. Título")
    print("2. Autor")
    print("3. Ano")
    print("4. Disponibilidade")
    print("5. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        novo_valor = input("Digite o novo título: ")
        atualizar_livros("titulo", novo_valor, id)

    elif opcao == "2":
        novo_valor = input("Digite o novo autor: ")
        atualizar_livros("autor", novo_valor, id)

    elif opcao == "3":
        novo_valor = input("Digite o novo ano: ")
        atualizar_livros("ano", novo_valor, id)

    elif opcao == "4":
        disponivel = input("O livro está disponível? (sim/não): ").strip().lower()
        if disponivel in ["sim", "não", "nao"]:
            atualizar_livros("disponivel", disponivel, id)
        else:
            print("Valor inválido para disponibilidade.")

    elif opcao == "5":
        print("Saindo da atualização.")
        break

    else:
        print("Opção inválida. Tente novamente.")
"""

deletar =  int(input("Informe o ID do livro que deseja deletar: "))
deletar_livro(deletar)