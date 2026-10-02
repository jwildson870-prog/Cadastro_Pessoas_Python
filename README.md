# 🐍 Cadastro Pessoas Python

## 📋 Sobre o Projeto

Sistema de cadastro de pessoas desenvolvido em **Python**, utilizando **Programação Orientada a Objetos (POO)**, JSON, validações, backup e sistema de logs.

O projeto foi desenvolvido com foco em aprendizado, organização de código e aplicação de conceitos de Python em um sistema funcional.

## 🎥 Demonstração

### Sistema em funcionamento

Demonstração do sistema de cadastro de pessoas funcionando através do terminal.

```text
╔══════════════════════════╗
║     SISTEMA DE PESSOAS   ║
╠══════════════════════════╣
║ 1 - Cadastrar            ║
║ 2 - Listar               ║
║ 3 - Buscar               ║
║ 4 - Editar               ║
║ 5 - Excluir              ║
║ 6 - Sair                 ║
╚══════════════════════════╝
```

> 📌 Uma demonstração em vídeo ou GIF pode ser adicionada posteriormente.

## ⚙️ Funcionalidades

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

## 📁 Estrutura do Projeto

```text
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
```

## 🧩 Organização dos Arquivos

### `main.py`

Arquivo principal responsável pelo menu e pela execução do sistema.

### `pessoa.py`

Contém a classe `Pessoa` e a estrutura dos dados de cada pessoa.

### `cadastro.py`

Responsável pelas operações de:

- Cadastrar
- Listar
- Buscar
- Editar
- Excluir

### `banco.py`

Responsável pelo armazenamento e gerenciamento dos dados:

- Carregar dados
- Salvar dados
- Criar backup
- Gerar IDs únicos

### `validacoes.py`

Contém funções reutilizáveis responsáveis pela validação dos dados informados pelo usuário.

## 💾 Armazenamento de Dados

### `pessoas.json`

Armazena os dados atuais das pessoas cadastradas.

### `pessoas_backup.json`

Armazena uma cópia anterior dos dados.

### `sistema.log`

Registra operações e acontecimentos importantes do sistema.

## 🛠️ Tecnologias Utilizadas

### Linguagem

- 🐍 Python 3

### Bibliotecas

- `json`
- `os`
- `uuid`
- `logging`
- `shutil`
- `datetime`

### Conceitos

- Programação Orientada a Objetos
- Classes e objetos
- Métodos
- Funções
- Modularização
- Validação de dados
- Persistência de dados
- Manipulação de arquivos
- Geração de IDs
- Sistema de logs
- Backup

### Ferramentas

- Git
- GitHub
- Termux

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/jwildson870-prog/Cadastro_Pessoas_Python.git
```

### 2. Entre na pasta

```bash
cd Cadastro_Pessoas_Python
```

### 3. Execute o sistema

```bash
python main.py
```

## 🎯 Objetivo

### Objetivo Principal

Praticar Python através do desenvolvimento de um sistema real de cadastro de pessoas.

### Conceitos Praticados

- Classes
- Objetos
- Métodos
- Modularização
- JSON
- UUID
- Logs
- Backup
- Validação
- Git
- GitHub

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos importantes para a construção de aplicações Python organizadas e reutilizáveis.

O projeto também serve como base para futuras implementações, como banco de dados SQLite, autenticação de usuários, interface gráfica e novas funcionalidades.

## 👨‍💻 Autor

### José Wildson

GitHub: [@jwildson870-prog](https://github.com/jwildson870-prog)

---

⭐ Projeto desenvolvido para estudos e prática de Python.
