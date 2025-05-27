import requests

def cotacao():
    
    moeda = input("Digite a moeda que deseja saber a cotação: ")
    moeda = moeda.upper()
    resposta = requests.get("https://economia.awesomeapi.com.br/json/last/{}-BRL".format(moeda))
    cotacao = resposta.json()

    nome = cotacao[moeda+"BRL"]['name']
    maximo = float(cotacao[moeda+"BRL"]['high'])
    baixo = float(cotacao[moeda+"BRL"]['low'])
    compra = float(cotacao[moeda+"BRL"]['bid'])
    horario = cotacao[moeda+"BRL"]['create_date']
    print("Conversão: {}\nValor máximo: R$ {:.2f}\nValor mínimo: R$ {:.2f}\nCompra: R$ {:.2f}\nAtualizado: {}".format(nome,maximo,baixo,compra,horario))

cotacao()