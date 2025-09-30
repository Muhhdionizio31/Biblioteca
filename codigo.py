import sqlite3
import funcoes as op
import streamlit as st
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

st.title("📚 Sistema de Biblioteca")
dados = op.listar_livros
menu = ["Cadastrar Livro", "Listar Livros", "Atualizar Livro", "Remover Livro"]
escolha = st.sidebar.selectbox("Menu", menu)

    # Cadastrar Livros
if escolha == "Cadastrar Livro":
    st.header("Cadastrar Novo Livro")
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.text_input("Ano")
    disponivel = st.selectbox("Disponibilidade", ["Sim", "Não"])

    if st.button("Cadastrar"):
        if titulo and autor and ano:
            op.cadastrar_livros(titulo.capitalize(), autor.capitalize(), ano.capitalize(), disponivel.capitalize())
        else:
            st.warning("Preencha todos os campos!")

    # Listar Livros
elif escolha == "Listar Livros":
    st.header("📖 Lista de Livros")
    dados = op.listar_livros()
    if dados:
        st.table(dados)
    else:
        st.info("Nenhum livro cadastrado.")

    # Atualizar Livros
elif escolha == "Atualizar Livro":
    st.header("✏️ Atualizar Livro")
    dados = op.listar_livros()
    if dados:
        st.dataframe(dados)
        id = st.number_input("Digite o ID do livro a ser atualizado:", min_value=1, step=1)
        campo = st.selectbox(f"Campo a atualizar", ["titulo", "autor", "ano", "disponivel"])
        novo_valor = st.text_input("Novo valor")

        if st.button("Atualizar"):
            op.atualizar_livros(campo, novo_valor, id)
    else:
        st.info("Nenhum livro para atualizar.")

    # Remover Livro
elif escolha == "Remover Livro":
    st.header("🗑 Remover Livro")
    dados = op.listar_livros()
    if dados:
        st.dataframe(dados)
        id = st.number_input("Digite o ID do livro a ser removido:", min_value=1, step=1)
        if st.button("Remover"):
            op.deletar_livro(id)
    else:
        st.warning("Nenhum livro para remover.")
