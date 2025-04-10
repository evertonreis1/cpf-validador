from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/health')
def health_check():
    return '', 200

def validar_cpf(cpf):
    # Remove all non-digit characters
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Check if length is 11 digits
    if len(cpf) != 11:
        return False
    
    # Check if all digits are the same (invalid CPF)
    if cpf == cpf[0] * 11:
        return False
    
    # Calculate first verification digit
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto > 9:
        resto = 0
    if resto != int(cpf[9]):
        return False
    
    # Calculate second verification digit
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto > 9:
        resto = 0
    if resto != int(cpf[10]):
        return False
    
    return True

@app.route('/validar', methods=['POST'])
def validar():
    data = request.get_json()
    cpf = data.get('cpf', '')
    valido = validar_cpf(cpf)
    return jsonify({'cpf': cpf, 'valido': valido})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
