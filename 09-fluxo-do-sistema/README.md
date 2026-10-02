# 09 — Fluxo completo do sistema

## 🧭 Visão geral

Imagine que o usuário escolhe **Cadastrar**.

O fluxo é:

```text
Usuário
  ↓
main.py
  ↓
cadastro.cadastrar()
  ↓
validar_texto()
  ↓
validar_idade()
  ↓
BancoDeDados.gerar_id()
  ↓
Pessoa(...)
  ↓
banco.pessoas.append()
  ↓
banco.salvar()
  ↓
Pessoa.to_dict()
  ↓
json.dump()
  ↓
pessoas.json
```

## 📋 E quando o usuário lista?

```text
main.py
  ↓
cadastro.listar()
  ↓
banco.pessoas
  ↓
for pessoa in ...
  ↓
print()
```

Nesse caso não é necessário ler o arquivo novamente, porque os objetos já foram carregados quando `BancoDeDados` foi criado.

## 🔎 E na inicialização?

```text
Cadastro()
   ↓
BancoDeDados()
   ↓
carregar()
   ↓
pessoas.json
   ↓
json.load()
   ↓
Pessoa.from_dict()
   ↓
lista de objetos Pessoa
```

## 🧠 Por que essa visão é importante?

Um iniciante pode olhar para cinco arquivos e achar que são programas separados. Na realidade, eles formam um único sistema.

Cada módulo responde a uma pergunta diferente:

| Pergunta | Módulo |
|---|---|
| Como o programa começa? | `main.py` |
| O que é uma pessoa? | `pessoa.py` |
| O que posso fazer com pessoas? | `cadastro.py` |
| Onde os dados ficam? | `banco.py` |
| Como evitar entradas inválidas? | `validacoes.py` |

## 🔁 Ciclo de vida de um registro

```text
Entrada → Validação → Objeto → Lista → JSON
                                      ↓
                                  Backup
```

Depois, em uma nova execução:

```text
JSON → Dicionário → Pessoa → Lista
```
