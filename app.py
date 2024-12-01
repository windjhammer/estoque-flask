from flask import Flask, request
import mariadb
import json
import os

app = Flask(__name__)

# Conexão com o banco usando variáveis de ambiente
conn = mariadb.connect(
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    host=os.getenv("DB_HOST", "127.0.0.1"),
    port=int(os.getenv("DB_PORT", 3306)),
    database=os.getenv("DB_NAME", "estoque")
)

conn.autocommit = False
cursor = conn.cursor(dictionary=True)

# CRUD
@app.route('/', methods=['GET'])
def hello_world():
    return 'Endpoint teste.', 200


@app.route('/registrar', methods=['POST'])
def registrar_produto():
    data = request.get_json()
    for i in data["produtos"]:
        cursor.execute(
            f"INSERT INTO produtos (quantidade, nome_produto, preco, categoria) VALUES ({i['quantidade']}, '{i['nome_produto']}', {i['preco']}, '{i['categoria']}')"
        )
    conn.commit()
    cursor.execute("SELECT id, nome_produto FROM produtos")
    produtos = cursor.fetchall()
    produtos_json = json.dumps(produtos)
    return produtos_json, 200


@app.route('/produtos', methods=['GET'])
def retorna_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        produto['preco'] = float(produto['preco'])
    return json.dumps(produtos), 200


@app.route('/atualizar', methods=['PUT'])
def atualizar_produto():
    data = request.get_json()
    cursor.execute(
        f"UPDATE produtos SET quantidade={data['quantidade']}, nome_produto='{data['nome_produto']}', preco={data['preco']}, categoria='{data['categoria']}' WHERE nome_produto LIKE '{data['nome_produto_antes']}'"
    )
    conn.commit()
    cursor.execute(f"SELECT * FROM produtos WHERE nome_produto LIKE '{data['nome_produto']}'")
    produto_atualizado = cursor.fetchone()
    return json.dumps(produto_atualizado), 200


@app.route('/apagar', methods=['DELETE'])
def delete_produto():
    params = request.args.to_dict()
    _id = params["id"]
    cursor.execute(f"DELETE FROM produtos WHERE id={_id}")
    conn.commit()
    return "OK", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

