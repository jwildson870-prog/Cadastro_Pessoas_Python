# 02 — Estrutura do projeto

## 📁 Arquivos principais

```text
Cadastro_Pessoas_Python/
├── main.py
├── pessoa.py
├── cadastro.py
├── banco.py
├── validacoes.py
├── pessoas.json
├── pessoas_backup.json
├── sistema.log
├── README.md
└── __pycache__/
```

## `main.py`

É o ponto de entrada do programa. Cria um objeto `Cadastro`, apresenta o menu e fica esperando as escolhas do usuário.

## `pessoa.py`

Define a classe `Pessoa`. É o modelo dos registros.

## `cadastro.py`

Concentra as operações que o usuário solicita: cadastrar, listar, buscar, editar e excluir.

## `banco.py`

Gerencia a lista de objetos e a comunicação com o arquivo JSON. Também cria backup e gera IDs.

## `validacoes.py`

Centraliza funções que verificam entradas digitadas pelo usuário.

## `pessoas.json`

É o arquivo que representa os dados persistidos atualmente.

## `pessoas_backup.json`

É uma cópia do JSON anterior ao salvamento.

## `sistema.log`

Foi preparado para receber registros de atividades usando o módulo `logging`. No estado recebido, o arquivo está vazio.

## `__pycache__`

É criado pelo Python para armazenar arquivos compilados (`.pyc`). Não é necessário estudar seu conteúdo para entender a aplicação.

## 🔗 Dependências entre módulos

```text
main.py
  └── cadastro.py
       ├── pessoa.py
       ├── banco.py
       │    └── pessoa.py
       └── validacoes.py
```

Essa divisão evita colocar todo o programa em um único arquivo e ajuda a separar responsabilidades.
