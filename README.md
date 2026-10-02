🐍 Cadastro Pessoas Python

📋 Sobre o Projeto

Sistema de cadastro de pessoas desenvolvido em Python, utilizando Programação Orientada a Objetos (POO), JSON, validações, backup e sistema de logs.

⚙️ Funcionalidades

- 👤 Cadastro de pessoas
- 📋 Listagem de pessoas
- 🔎 Busca por nome, ID ou idade
- ✏️ Edição de cadastro
- 🗑️ Exclusão de cadastro
- 🆔 Geração automática de IDs únicos
- 💾 Persistência dos dados em JSON
- 🔄 Backup automático
- 📝 Sistema de logs
- ✅ Validação dos dados
- 🧩 Código dividido em módulos

📁 Estrutura do Projeto

Cadastro_Pessoas_Python/
│
├── main.py
├── pessoa.py
├── cadastro.py
├── banco.py
├── validacoes.py
│
├── pessoas.json
├── pessoas_backup.json
├── sistema.log
│
└── README.md

🧩 Organização dos Arquivos

"main.py"

Arquivo principal responsável pelo menu e execução do sistema.

"pessoa.py"

Contém a classe "Pessoa" e a estrutura dos dados de cada pessoa.

"cadastro.py"

Responsável pelas operações de cadastro:

- Cadastrar
- Listar
- Buscar
- Editar
- Excluir

"banco.py"

Responsável pelo armazenamento dos dados:

- Carregar JSON
- Salvar JSON
- Criar backup
- Gerar IDs únicos

"validacoes.py"

Contém as funções responsáveis pela validação dos dados informados pelo usuário.

💾 Armazenamento de Dados

"pessoas.json"

Armazena os dados atuais das pessoas cadastradas.

"pessoas_backup.json"

Armazena uma cópia anterior dos dados.

"sistema.log"

Registra as operações e acontecimentos do sistema.

🛠️ Tecnologias Utilizadas

#Linguagem

#- 🐍 Python 3

##Conceitos

- Programação Orientada a Objetos
- Classes e objetos
- Funções
- Modularização
- Validação de dados
- Persistência de dados

##Bibliotecas

- "json"
- "os"
- "uuid"
- "logging"
- "shutil"
- "datetime"

##Ferramentas

- Git
- GitHub
- Termux

##▶️ Como Executar

##1. Clone o repositório

git clone https://github.com/jwildson870-prog/Cadastro_Pessoas_Python.git

$$2. Entre na pasta

cd Cadastro_Pessoas_Python

##3. Execute o sistema

python main.py

#🎯 Objetivo

##Objetivo Principal

Praticar Python através do desenvolvimento de um sistema real de cadastro.

##Conceitos Praticados

- Classes
- Objetos
- Métodos
- Modularização
- JSON
- UUID
- Logs
- Backup
- Validação
- Git e GitHub

#👨‍💻 Autor

##José Wildson

##GitHub: "@jwildson870-prog" (https://github.com/jwildson870-prog)

---

⭐ Projeto desenvolvido para estudos e prática de Python.
