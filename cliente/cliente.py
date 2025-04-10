import requests

cpf = input("Digite um CPF para validar: ")
res = requests.post("http://localhost:5000/validar", json={"cpf": cpf})

print("Resposta do servidor:", res.json())
