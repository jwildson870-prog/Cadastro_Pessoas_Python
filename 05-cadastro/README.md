# 05 — Entendendo `cadastro.py`

## 🧠 Responsabilidade

A classe `Cadastro` reúne as operações que fazem sentido para o usuário.

No construtor:

```python
self.banco = BancoDeDados()
```

O cadastro recebe um objeto responsável pelo armazenamento.

## ➕ Cadastrar

O método `cadastrar()` segue esta sequência:

```text
pedir nome
   ↓
validar nome
   ↓
pedir idade
   ↓
validar idade
   ↓
verificar duplicidade de nome
   ↓
gerar ID
   ↓
criar Pessoa
   ↓
adicionar à lista
   ↓
salvar JSON
```

## 📋 Listar

`listar()` verifica se existe alguma pessoa. Se existir, percorre:

```python
for pessoa in self.banco.pessoas:
```

e exibe os atributos.

## 🔎 Buscar

O usuário escolhe:

```text
1 - nome
2 - ID
3 - idade
```

Na busca por nome, o programa transforma o texto para minúsculas e usa `in`, permitindo encontrar um trecho do nome.

Exemplo conceitual:

```python
if nome in pessoa.nome.lower():
```

Assim, uma busca por `jo` pode encontrar `João`.

## ✏️ Editar

O método procura a pessoa, altera:

```python
pessoa.nome = nome
pessoa.idade = idade
```

e depois chama `self.banco.salvar()`.

## 🗑️ Excluir

Antes de remover o objeto, o método chama `confirmar()` para solicitar `S` ou `N`.

Se confirmado:

```python
self.banco.pessoas.remove(pessoa)
```

Depois os dados são salvos novamente.

## ⚠️ Atenção ao ID no código atual

O arquivo `banco.py` cria IDs como texto, por exemplo:

```text
089c4710
```

Mas `cadastro.py` usa `validar_numero()` para receber o ID, e essa função converte a entrada para `int`. Portanto, a comparação entre o ID textual e o número inteiro pode não encontrar o registro.

Esse é um ponto importante para quem estiver estudando ou corrigindo o projeto.
