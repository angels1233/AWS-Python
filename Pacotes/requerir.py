import requests
import json

reposta = requests.get("https://randomuser.me/api/")
pessoa = reposta.json()

usuario = pessoa['results'][0]
nome = "{} {}".format(usuario['name']['first'], usuario['name']['last'])
email = "{}".format(usuario['email'])
endereco = "{} {}".format(usuario['location']['state'], usuario['location']['country'])

print(nome)
print(email)
print(endereco)