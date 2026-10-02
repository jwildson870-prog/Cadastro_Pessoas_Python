# 11 — Como estudar este projeto

## 🎓 Etapa 1 — Entenda o objetivo

Antes de olhar o código, saiba responder:

> O programa cadastra pessoas, guarda os dados e permite consultar, editar e excluir registros.

## 🎓 Etapa 2 — Estude `pessoa.py`

Aprenda primeiro:

- classe;
- `__init__`;
- atributos;
- objeto;
- `to_dict()`;
- `from_dict()`.

## 🎓 Etapa 3 — Estude `validacoes.py`

Depois entenda como o programa recebe dados do usuário sem aceitar qualquer entrada.

Preste atenção em `try`/`except`.

## 🎓 Etapa 4 — Estude `banco.py`

Agora acompanhe a persistência:

```text
lista Python ↔ JSON
```

Entenda `load`, `dump`, backup e UUID.

## 🎓 Etapa 5 — Estude `cadastro.py`

Com as peças anteriores compreendidas, fica mais fácil entender as regras de negócio.

Leia um método por vez:

1. `cadastrar()`;
2. `listar()`;
3. `buscar()`;
4. `editar()`;
5. `excluir()`.

## 🎓 Etapa 6 — Estude `main.py`

Por último, veja como tudo é chamado pelo menu.

## 🧪 Exercícios recomendados

### Fácil

1. Adicione um campo `cidade` à classe `Pessoa`.
2. Mostre a cidade na listagem.
3. Salve a cidade no JSON.

### Médio

1. Crie busca por cidade.
2. Impedir cadastro de duas pessoas com o mesmo nome e idade.
3. Crie uma função para contar quantas pessoas existem.

### Mais avançado

1. Corrija o tratamento dos IDs.
2. Configure o `logging` para gravar corretamente em `sistema.log`.
3. Separe as mensagens da interface da lógica de negócio.
4. Migre o armazenamento de JSON para SQLite.

## 💡 Regra de estudo

Não tente decorar o projeto inteiro. Entenda o caminho dos dados.

```text
entrada → validação → objeto → armazenamento → saída
```

Quando esse caminho estiver claro, os detalhes do código ficam muito mais fáceis.
