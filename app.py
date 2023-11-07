from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes',
        'valor': 'R$50.00'
    },
    {
        'id': 2,
        'titulo': 'Hamlet',
        'autor': 'William Shakespeare',
        'valor': 'R$150.00'
    },
    {
        'id': 3,
        'titulo': 'Os Lusiadas',
        'autor': 'Luis Camoes',
        'valor': 'R$115.00'
    },
]

# Criando as rotas para realizar as operações CRUD
# Rota para Consultar todos os livros
@app.route('/livros', methods = ['GET'])
def listar_livros():
    return jsonify(livros)

# Rota para Consultar livro por passagem de id
@app.route('/livros/<int:id>', methods=['GET'])
def id_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
# Rota para Criar livros
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Rota para Editar livros já cadastrados a partir do parâmetro id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    alterar_livro = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(alterar_livro)
            return jsonify(livros[indice])

# Rota para Excluir livros a partir do id
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)