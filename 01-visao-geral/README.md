# 01 — Visão geral do projeto

## 🐍 O que é este projeto?

O projeto é um **sistema de cadastro de pessoas executado no terminal**, escrito em Python.

Ele permite armazenar pessoas com:

- ID;
- nome;
- idade;
- data e hora do cadastro.

Além de cadastrar, o sistema possui operações de consulta e manutenção dos registros.

## ⚙️ O que o usuário consegue fazer?

O menu principal apresenta seis opções:

```text
1 - Cadastrar
2 - Listar
3 - Buscar
4 - Editar
5 - Excluir
6 - Sair
```

### Cadastrar

O programa pede nome e idade, verifica se os dados são válidos, cria um ID e adiciona um objeto `Pessoa` à lista.

### Listar

Percorre a lista de pessoas e mostra os dados de cada objeto.

### Buscar

Permite tentar encontrar pessoas pelo nome, ID ou idade.

### Editar

Localiza uma pessoa e permite alterar nome e idade.

### Excluir

Localiza uma pessoa, pede confirmação e remove o objeto da lista.

## 💾 O sistema guarda os dados?

Sim. Os dados são armazenados em `pessoas.json`. Quando o programa salva alterações, uma cópia do arquivo anterior é criada em `pessoas_backup.json`.

## 🧩 Por que o projeto é interessante para estudar Python?

Porque ele junta vários assuntos em um único programa:

- funções;
- classes;
- objetos;
- métodos;
- listas;
- dicionários;
- `if`/`elif`/`else`;
- `for` e `while`;
- `match`;
- `try`/`except`;
- arquivos;
- JSON;
- módulos e imports;
- datas;
- UUID;
- logging;
- validação.

## 🧠 Ideia principal

A melhor forma de entender o sistema é pensar em quatro camadas:

```text
USUÁRIO
   ↓
main.py
   ↓
cadastro.py
   ↓
banco.py + pessoa.py + validacoes.py
   ↓
pessoas.json
```

O usuário escolhe uma operação. `main.py` encaminha a escolha. `cadastro.py` executa a regra da operação. `banco.py` cuida da persistência, enquanto `Pessoa` representa os dados.
