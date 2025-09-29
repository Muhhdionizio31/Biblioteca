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

