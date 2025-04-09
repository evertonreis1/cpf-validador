import requests
import time

time.sleep(5)

cpf = input("Digite um CPF para validar: ")
res = requests.post("http://servidor:5000/validar", json={"cpf": cpf})

print("Resposta do servidor:", res.json())
