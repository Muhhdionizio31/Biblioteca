import sqlite3
import funcoes as op

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

# Loop do menu principal
while True:
    print("\n---- Sistema da Biblioteca ----")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Atualizar Livro")
    print("4. Remover Livro")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ").strip().lower()
        autor = input("Digite o autor do livro: ").strip().lower()
        ano = input("Digite o ano do livro: ").strip().lower()
        disponivel = input("O livro está disponível? (sim/não): ").strip().lower()

        op.cadastrar_livros(titulo, autor, ano, disponivel)

    elif opcao == "2":
        op.listar_livros()

    elif opcao == "3":
        id = int(input("Digite o ID do livro que deseja atualizar: "))
        while True:
            print("\nO que deseja atualizar?")
            print("1. Título")
            print("2. Autor")
            print("3. Ano")
            print("4. Disponibilidade")
            print("5. Voltar ao menu principal")

            sub_opcao = input("Digite a opção desejada: ")

            if sub_opcao == "1":
                novo_valor = input("Digite o novo título: ")
                op.atualizar_livros("titulo", novo_valor, id)
            elif sub_opcao == "2":
                novo_valor = input("Digite o novo autor: ")
                op.atualizar_livros("autor", novo_valor, id)
            elif sub_opcao == "3":
                novo_valor = input("Digite o novo ano: ")
                op.atualizar_livros("ano", novo_valor, id)
            elif sub_opcao == "4":
                novo_valor = input("O livro está disponível? (sim/não): ").strip().lower()
                if novo_valor in ["sim", "não", "nao"]:
                    op.atualizar_livros("disponivel", novo_valor, id)
                else:
                    print("Valor inválido para disponibilidade.")
            elif sub_opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao == "4":
        try:
            deletar_id = int(input("Informe o ID do livro que deseja deletar: "))
            op.deletar_livro(deletar_id)
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

    elif opcao == "5":
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
