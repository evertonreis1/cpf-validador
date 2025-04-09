from flask import Flask, request, jsonify

app = Flask(__name__)

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11

@app.route('/validar', methods=['POST'])
def validar():
    data = request.get_json()
    cpf = data.get('cpf', '')
    valido = validar_cpf(cpf)
    return jsonify({'cpf': cpf, 'valido': valido})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
