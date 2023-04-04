from flask import Flask, jsonify, request
import datetime

pj = Flask(__name__)


class Usuario:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


usuarios = [Usuario
            (98729896568,
             "Miss Fortune",
             datetime.date(2010, 9, 8)), Usuario(64729896588,
                                                 "Caitlyn",
                                                 datetime.date(1998, 10, 1))]


@pj.route('/usuario', methods=['POST'])
def criar_usuario():
    dados = request.json
    cpf = dados['cpf']
    nome = dados['nome']
    data_nascimento = datetime.datetime.strptime(
        dados['data_nascimento'], '%d/%m/%Y').date()

    novo_usuario = Usuario(cpf, nome, data_nascimento)

    usuarios.append(novo_usuario)

    return jsonify({'mensagem': 'Usuario criado com sucesso'}), 201


@pj.route('/usuario/<int:cpf>', methods=['GET'])
def obter_usuario(cpf):

    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    if usuario is None:
        return jsonify({'mensagem': 'Usuario nao encontrado'}), 404

    return jsonify(usuario.__dict__), 200


pj.run(port=5000, host='localhost', debug=True)
