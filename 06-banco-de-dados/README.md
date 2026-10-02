# 06 — Entendendo `banco.py`

## 💾 Por que existe um módulo de banco?

O programa precisa guardar informações depois que termina. A classe `BancoDeDados` centraliza essa tarefa.

Ela possui:

```python
self.pessoas = []
```

A lista mantém os objetos `Pessoa` durante a execução.

## 📥 Carregamento

Ao criar `BancoDeDados`, o construtor chama:

```python
self.carregar()
```

Se `pessoas.json` existir, o programa usa:

```python
json.load(arquivo)
```

para transformar o conteúdo JSON em dados Python.

Cada registro é convertido novamente em objeto:

```python
Pessoa.from_dict(dados_pessoa)
```

## 💾 Salvamento

O método `salvar()` primeiro verifica se o arquivo atual existe.

Se existir, faz:

```python
shutil.copy(ARQUIVO, BACKUP)
```

Depois transforma cada objeto em dicionário usando `to_dict()` e grava o resultado com `json.dump()`.

## 🔐 Backup

O backup é uma cópia do arquivo anterior ao salvamento. Isso significa que ele funciona como uma pequena camada de segurança contra perda imediata do estado anterior.

## 🆔 Geração de ID

O código usa:

```python
uuid.uuid4().hex[:8]
```

`uuid4()` gera um identificador aleatório. `.hex` produz sua representação hexadecimal e `[:8]` pega apenas os primeiros oito caracteres.

## ⚠️ Observação sobre IDs

Como o resultado é texto, ele precisa ser tratado como `str` em todas as operações de busca, edição e exclusão. No estado atual do projeto, essas três operações recebem o ID através de `validar_numero()`, que retorna `int`. Essa inconsistência deve ser corrigida em uma futura versão.

## 🧯 Tratamento de erros

O carregamento trata erros como:

- `json.JSONDecodeError`;
- `KeyError`;
- `TypeError`.

O salvamento trata `OSError`.
