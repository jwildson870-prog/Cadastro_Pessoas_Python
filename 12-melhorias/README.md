# 12 — Melhorias e pontos de atenção

Esta documentação também deve mostrar o que pode ser aprimorado. Um projeto de estudo não precisa estar perfeito para ser útil; identificar problemas faz parte do aprendizado.

## ⚠️ 1. Inconsistência no ID

`BancoDeDados.gerar_id()` retorna uma `str` de oito caracteres hexadecimais.

Porém, `cadastro.py` usa `validar_numero()` para receber o ID, transformando a entrada em `int`.

Isso pode fazer comparações como esta falharem:

```python
if pessoa.id == id_pessoa:
```

### Como melhorar

Criar uma função específica para ID que retorne texto, por exemplo:

```python
def validar_id(mensagem):
    valor = input(mensagem).strip()
    if not valor:
        erro("Digite um ID.")
        return None
    return valor
```

Assim o tipo usado na comparação fica consistente.

## ⚠️ 2. Configuração do logging

O projeto chama `logging.info()` e `logging.error()`, mas não configura explicitamente o destino do log.

### Como melhorar

Configurar o `logging` no ponto de entrada, definindo arquivo, nível e formato.

## ⚠️ 3. `clear` específico de Unix

```python
os.system("clear")
```

Funciona em ambientes Unix/Linux, mas não é a solução ideal para todos os sistemas.

### Como melhorar

Detectar o sistema operacional ou criar uma função compatível com Windows e Unix.

## ⚠️ 4. Validação de nomes

`isalpha()` pode rejeitar alguns nomes legítimos que contenham caracteres fora da categoria esperada pelo método.

Também não existe uma regra de tamanho mínimo ou máximo.

## ⚠️ 5. Busca por nome

A busca parcial é útil, mas poderia ter opções para busca exata e ordenação.

## ⚠️ 6. Segurança e concorrência

JSON é adequado para um projeto pequeno de estudo, mas não é ideal como banco de dados para muitos usuários ou acessos simultâneos.

## 🚀 Evoluções possíveis

Uma evolução natural seria:

```text
Terminal + JSON
       ↓
Terminal + SQLite
       ↓
Aplicação web
       ↓
Banco de dados real
       ↓
Autenticação + usuários + permissões
```

Outras ideias:

- exportação CSV;
- relatórios;
- ordenação por nome ou idade;
- paginação;
- testes automatizados;
- interface gráfica;
- API;
- banco SQLite;
- documentação automática;
- tratamento de exceções mais detalhado.

## ✅ O mais importante

As melhorias não diminuem o valor do projeto atual. Pelo contrário: elas mostram exatamente quais conceitos podem ser estudados na próxima versão.
