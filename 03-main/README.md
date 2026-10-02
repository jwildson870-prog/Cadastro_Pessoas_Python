# 03 — Entendendo o `main.py`

## 🎮 Função do arquivo

`main.py` controla a interação principal com o usuário.

Ele importa:

```python
import os
from cadastro import Cadastro
from validacoes import validar_numero
```

Depois cria:

```python
cadastro = Cadastro()
```

Isso faz com que o objeto `Cadastro` seja criado antes do menu começar.

## 🧹 `limpar_tela()`

```python
def limpar_tela():
    os.system("clear")
```

A função executa o comando `clear` do sistema operacional. Ela foi escrita pensando principalmente em terminais Unix/Linux, como Termux.

## ⏸️ `pausar()`

```python
def pausar():
    input("\nPressione ENTER para continuar...")
```

O programa espera o usuário pressionar ENTER.

## ❌ `erro()`

Recebe uma mensagem, mostra o erro, espera ENTER e limpa a tela.

## 🔁 Laço principal

O trecho:

```python
while True:
```

faz o menu continuar aparecendo indefinidamente.

A repetição só termina quando ocorre:

```python
case 6:
    break
```

## 🧭 `match`

O código usa `match` para escolher uma ação de acordo com o número informado.

```python
match escolha:
    case 1:
        cadastro.cadastrar()
    case 2:
        cadastro.listar()
```

É uma alternativa organizada para uma sequência grande de `if`/`elif`.

## 🧠 Papel do `main.py`

Uma ideia importante: `main.py` **não implementa toda a lógica do cadastro**. Ele apenas coordena o programa. Isso é uma característica de modularização.
