import requests


def cep():

    cep = input("Digite o cep sem potuação: ")
    resposta = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    endereco = resposta.json()

    logradouro = endereco["logradouro"]
    bairro = endereco['bairro']
    cidade = endereco['localidade']
    estado =endereco['estado']

    print("Rua: {}\nBairro: {}\nCidade: {}\nEstado: {}".format(logradouro,bairro,cidade,estado))

cep()
