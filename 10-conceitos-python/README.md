# 10 — Conceitos de Python presentes no projeto

## 1. Variáveis

Exemplo:

```python
nome = validar_texto("Nome: ")
```

A variável `nome` guarda o valor retornado pela função.

## 2. Funções

O projeto possui várias funções reutilizáveis, como `validar_numero()`, `validar_idade()` e `limpar_tela()`.

## 3. Classes

`Pessoa` e `Cadastro` são classes.

## 4. Objetos

```python
pessoa = Pessoa(nome, idade, id_pessoa)
```

Aqui, `pessoa` é um objeto da classe `Pessoa`.

## 5. Métodos

Funções definidas dentro de classes são métodos, como `cadastrar()`, `listar()` e `salvar()`.

## 6. Listas

```python
self.pessoas = []
```

A lista mantém várias pessoas.

## 7. Dicionários

`to_dict()` retorna um dicionário. Dicionários também aparecem no conteúdo carregado do JSON.

## 8. `for`

Usado para percorrer pessoas:

```python
for pessoa in self.banco.pessoas:
```

## 9. `while`

Usado para manter o menu e a confirmação funcionando até uma condição de saída.

## 10. `try` / `except`

Usado para lidar com entradas inválidas e erros de arquivos.

## 11. Imports

Os arquivos são conectados com `from ... import ...`.

## 12. Decorador `@classmethod`

`from_dict()` usa `@classmethod`, permitindo construir um objeto a partir dos dados recebidos sem precisar de uma instância existente.

## 13. Módulos da biblioteca padrão

O projeto usa recursos nativos do Python, como:

- `os`;
- `json`;
- `shutil`;
- `logging`;
- `uuid`;
- `datetime`.

## 14. Modularização

Em vez de colocar tudo em `main.py`, o código foi separado por responsabilidade. Esse é um dos aprendizados centrais do projeto.
