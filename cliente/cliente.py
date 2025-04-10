import requests

print("Bem-vindo ao sistema de validação de CPF. Para sair, digite 'sair'.")

while True:
    cpf = input("\nDigite um CPF para validar: ")
    if cpf == 'sair':
        break

    res = requests.post("http://localhost:5000/validar", json={"cpf": cpf})
    res = res.json()

    if res['valido']:
        print(f"CPF \"{cpf}\" é válido.")
    else:
        print(f"CPF \"{cpf}\" é inválido.")
