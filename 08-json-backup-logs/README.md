# 08 — JSON, backup e logs

## 🗃️ `pessoas.json`

O arquivo atual contém uma lista de objetos representados como dicionários JSON.

Exemplo simplificado:

```json
[
    {
        "id": "089c4710",
        "nome": "José",
        "idade": 18,
        "data_cadastro": "02/10/2026 04:06"
    }
]
```

## 🔄 JSON e Python

O projeto utiliza duas funções fundamentais:

```python
json.load(arquivo)
```

para ler JSON, e:

```python
json.dump(dados, arquivo, ensure_ascii=False, indent=4)
```

para escrever JSON.

`ensure_ascii=False` ajuda a preservar caracteres como `José` corretamente, enquanto `indent=4` deixa o arquivo organizado.

## 🛡️ `pessoas_backup.json`

Antes de substituir o arquivo principal, o sistema copia o estado anterior para o backup.

Isso permite manter uma versão imediatamente anterior dos dados.

## 📝 `sistema.log`

O código usa chamadas como:

```python
logging.info("Dados salvos com sucesso.")
```

ou:

```python
logging.error(f"Erro ao salvar dados: {erro}")
```

Porém, no estado recebido, não existe uma configuração explícita como `logging.basicConfig(...)`. Além disso, o arquivo `sistema.log` está vazio. Portanto, o código demonstra o uso de `logging`, mas a configuração efetiva do arquivo de log precisa ser revisada para garantir que os registros sejam gravados nele.
