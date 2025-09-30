📚 Sistema de Biblioteca

Um sistema simples de gerenciamento de livros utilizando Python, Streamlit e SQLite. Com ele, é possível cadastrar, listar, atualizar e remover livros de um banco de dados local.

🛠 Funcionalidades

Cadastrar Livro: Insere um novo livro no banco de dados.

Listar Livros: Exibe todos os livros cadastrados.

Atualizar Livro: Permite editar informações de um livro.

Remover Livro: Exclui um livro da base de dados.

📦 Tecnologias Utilizadas

Python

Streamlit

SQLite3

▶️ Como Executar o Projeto

Clone o repositório:

git clone https://github.com/Muhhdionizio31/Biblioteca

Instale as dependências:

pip install streamlit


Execute o aplicativo:

python -m streamlit run codigo.py

📁 Estrutura do Projeto
biblioteca/
├── codigo.py               # Arquivo principal com a interface Streamlit
├── funcoes.py           # Funções auxiliares (CRUD com SQLite)
├── biblioteca.db        # Banco de dados SQLite (gerado automaticamente)
└── README.md            # Este arquivo

🧠 Como Funciona

Os dados são armazenados em um banco SQLite local (biblioteca.db).

A interface é feita com o Streamlit, sendo interativa e fácil de usar.

As ações de banco de dados (CRUD) estão separadas no arquivo funcoes.py, facilitando a manutenção do código.

📌 Observações

Certifique-se de que o arquivo funcoes.py está na mesma pasta que o codigo.py.

O banco de dados é criado automaticamente na primeira execução.

Para uma versão em produção, seria interessante aplicar melhorias como:

Validações mais robustas

Autenticação de usuários

Paginação da lista de livros

Exportação de dados