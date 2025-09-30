import sqlite3

def cadastrar_livros(titulo, autor, ano, disponivel):  # Agora aceita 4 argumentos
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO biblioteca (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, disponivel))
        conexao.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as e:
        print("Ocorreu um erro:", e)
    finally:
        if conexao:
            conexao.close()

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM biblioteca")
        for linha in cursor.fetchall():
            print(f"ID {linha[0]} | TÍTULO: {linha[1]} | AUTOR: {linha[2]} | ANO: {linha[3]} | DISPONIBILIDADE: {linha[4]}")
    except Exception as e:
        print("Ocorreu um erro:", e)
    finally:
        if conexao:
            conexao.close()

def atualizar_livros(campo, novo_valor, id):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        sql = f"UPDATE biblioteca SET {campo} = ? WHERE id = ?"
        cursor.execute(sql, (novo_valor, id))

        conexao.commit()
        print(f"{campo.capitalize()} atualizado com sucesso!")
    except Exception as e:
        print("Erro ao atualizar os dados:", e)
    finally:
        conexao.close()