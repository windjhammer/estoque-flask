# API de Gestão de Produtos - Loja de Material de Construção

Esta API foi criada com Python (Flask) e MariaDB para gerenciar produtos como por exemplo em uma loja de material de construção. O sistema permite realizar operações de CRUD (Create, Read, Update, Delete) para adicionar, listar, atualizar e apagar produtos de um banco de dados.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python para a criação da API.
- **MariaDB**: Banco de dados relacional para armazenar os produtos.
- **Docker**: Para facilitar o ambiente de desenvolvimento e execução, tanto do aplicativo Flask quanto do banco de dados MariaDB.
- **Docker Compose**: Para orquestrar os contêineres do Flask e MariaDB.

## Funcionalidades da API

A API expõe os seguintes endpoints para manipulação dos produtos:

### 1. **Criar Produtos (POST `/registrar`)**

Este endpoint permite adicionar novos produtos à base de dados. Ele espera um corpo JSON com uma lista de produtos, onde cada produto é um objeto com as seguintes propriedades:
- `quantidade`: Quantidade do produto no estoque.
- `nome_produto`: Nome do produto.
- `preco`: Preço unitário do produto.
- `categoria`: Categoria do produto (ex: "Cimento", "Ferramentas", etc.).

**Exemplo de Requisição:**
```json
{
  "produtos": [
    {
      "quantidade": 100,
      "nome_produto": "Cimento",
      "preco": 30.50,
      "categoria": "Construção"
    },
    {
      "quantidade": 50,
      "nome_produto": "Martelo",
      "preco": 25.00,
      "categoria": "Ferramentas"
    }
  ]
}
```
**Resposta Esperada**

```json
[
  {
    "id": 1,
    "nome_produto": "Cimento"
  },
  {
    "id": 2,
    "nome_produto": "Martelo"
  }
]
```

### 2. **Listar produtos (GET /produtos)**

**Exemplo de Requisição:**
```GET /produtos ```

**Resposta Esperada**

```json
[
  {
    "id": 1,
    "quantidade": 100,
    "nome_produto": "Cimento",
    "preco": 30.5,
    "categoria": "Construção"
  },
  {
    "id": 2,
    "quantidade": 50,
    "nome_produto": "Martelo",
    "preco": 25.0,
    "categoria": "Ferramentas"
  }
]
```
