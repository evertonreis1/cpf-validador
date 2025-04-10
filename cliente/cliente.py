import requests
import time

SERVER_URL = "http://servidor:5000"

def wait_for_server():
    while True:
        try:
            requests.get(f"{SERVER_URL}/health")
            print("Servidor está disponível!")
            return True
        except requests.exceptions.ConnectionError:
            print("Aguardando servidor ficar disponível...")
            time.sleep(1)

print("Bem-vindo ao sistema de validação de CPF. Para sair, digite 'sair'.")

# Wait for server to be available
wait_for_server()

while True:
    cpf = input("\nDigite um CPF para validar: ")
    if cpf == 'sair':
        break

    try:
        res = requests.post(f"{SERVER_URL}/validar", json={"cpf": cpf})
        res = res.json()

        if res['valido']:
            print(f"CPF \"{cpf}\" é válido.")
        else:
            print(f"CPF \"{cpf}\" é inválido.")
    except requests.exceptions.ConnectionError:
        print("Erro: Servidor não está disponível. Tentando reconectar...")
        wait_for_server()
