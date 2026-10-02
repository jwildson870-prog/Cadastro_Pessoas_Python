# 07 — Entendendo `validacoes.py`

## 🎯 Por que validar?

Sem validação, o usuário poderia deixar campos vazios ou informar dados em formatos inesperados. As funções deste arquivo tentam impedir isso.

## 🔤 `validar_texto()`

A função remove espaços extras das extremidades:

```python
valor = input(mensagem).strip()
```

Depois verifica se está vazio.

Também usa:

```python
valor.replace(" ", "").isalpha()
```

para permitir letras e espaços entre palavras.

## 🔢 `validar_numero()`

Tenta transformar a entrada em inteiro:

```python
valor = int(input(mensagem))
```

Se o usuário digitar algo como `abc`, ocorre `ValueError`, que é tratado pelo `except`.

O código também impede números negativos.

## 🎂 `validar_idade()`

Reaproveita `validar_numero()` e adiciona uma regra: idade acima de 120 é rejeitada.

Isso demonstra **reutilização de funções**.

## ❓ `confirmar()`

Fica repetindo a pergunta até receber `s` ou `n`.

```text
S → True
N → False
```

Essa função é usada antes da exclusão.

## 🔁 Relação com `try` e `except`

Um dos conceitos didáticos mais importantes está aqui:

```python
try:
    valor = int(input(mensagem))
except ValueError:
    ...
```

O programa tenta realizar uma operação que pode falhar. Se a falha esperada acontecer, ele trata o erro sem encerrar a aplicação.
