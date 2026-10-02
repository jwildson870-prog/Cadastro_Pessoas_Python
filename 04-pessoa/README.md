# 04 — Entendendo `pessoa.py`

## 👤 A classe `Pessoa`

A classe representa uma pessoa cadastrada.

```python
class Pessoa:
```

Uma classe funciona como um molde. Cada vez que o programa executa `Pessoa(...)`, ele cria um objeto baseado nesse molde.

## 🧱 Construtor

O método:

```python
def __init__(self, nome, idade, id, data_cadastro=None):
```

é executado quando um novo objeto é criado.

Ele recebe os dados e cria os atributos:

```python
self.id = id
self.nome = nome
self.idade = idade
```

## 🕒 Data do cadastro

Se nenhuma data for enviada, o programa gera automaticamente uma data atual:

```python
datetime.now().strftime("%d/%m/%Y %H:%M")
```

Isso produz um formato semelhante a:

```text
02/10/2026 04:30
```

## 🔄 `to_dict()`

JSON trabalha naturalmente com estruturas como listas e dicionários. Por isso o objeto possui:

```python
def to_dict(self):
```

Ele transforma a pessoa em um dicionário:

```python
{
    "id": self.id,
    "nome": self.nome,
    "idade": self.idade,
    "data_cadastro": self.data_cadastro
}
```

## 🔁 `from_dict()`

O caminho inverso também existe:

```python
@classmethod
def from_dict(cls, dados):
```

Ele recebe um dicionário vindo do JSON e cria um objeto `Pessoa`.

## 🔄 Ciclo completo

```text
Objeto Pessoa
     ↓ to_dict()
Dicionário
     ↓ json.dump()
Arquivo JSON
     ↓ json.load()
Dicionário
     ↓ from_dict()
Objeto Pessoa
```

Esse é um dos conceitos mais importantes do projeto: transformar dados entre objetos Python e dados persistidos.
