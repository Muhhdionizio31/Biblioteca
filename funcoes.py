import streamlit as st
import sqlite3

def cadastrar_livros(titulo, autor, ano, disponivel):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO biblioteca (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, disponivel))
        conexao.commit()
        st.success("Livro cadastrado com sucesso!")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM biblioteca")
        dados = cursor.fetchall()
        return dados
    except Exception as e:
        st.error(f"Erro ao listar livros: {e}")
    finally:
        conexao.close()

def atualizar_livros(campo, novo_valor, id):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE biblioteca SET {campo} = ? WHERE id = ?", (novo_valor, id))
        conexao.commit()
        st.success(f"{campo.capitalize()} atualizado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao atualizar: {e}")
    finally:
        conexao.close()

def deletar_livro(id):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM biblioteca WHERE id = ?", (id,))
        conexao.commit()
        if cursor.rowcount == 0:
            st.warning(f"Nenhum livro com ID {id}.")
        else:
            st.success(f"Livro com ID {id} deletado com sucesso.")
    except Exception as e:
        st.error(f"Erro ao deletar livro: {e}")
    finally:
        conexao.close()
