#variáveis globais
repetir = True
itens = 0
nomeProduto = []
precoProduto = []
qtdProduto = []

#Função pra retornar a pergunta caso a resposta seja diferente da esperada

def pergunta():
    resposta = input("Deseja adicionar mais produtos? (S/N):")
    global itens
    match(resposta.upper()):
        case "S":
            itens+=1
            return True
        case "N":
            return False
        case _:
            print("Resposta invalida!")
            return pergunta()

#Preenchimento dos produtos de forma que se repete de acordo com o usuário
while repetir:
    nomeProduto.append(input("Digite o nome do produto: "))  
    precoProduto.append(input("Informe o valor do produto: "))

    #Tratamento de erro caso o usuário coloque virgulo ao invez de ponto no valor
    try:
        precoProduto[itens] = float(precoProduto[itens])
    except:
        precoProduto[itens] = precoProduto[itens].replace(",",".")
        precoProduto[itens] = float(precoProduto[itens])
    qtdProduto.append(int(input("Informe a quantidade comprada: ")))
     
    repetir = pergunta()
        

#Função que organiza os produtos e faz o calculo de valor

def Notinha(produto, preco, qtd):
    global itens
    valorProdTotal = []
    subTotal = 0

    print("\n--------------------------Descrição--------------------------\n")
    for i in range(itens+1):
        valorProdTotal.append(preco[i]*qtd[i])
        subTotal+=valorProdTotal[i]
        
        print("{} --- {} --- UNIT {} --- Valor {:.2f} --- Total {:.2f}".format((i+1),produto[i],qtd[i],preco[i],valorProdTotal[i]))
    print("\nSubtotal: R$ {:.2f}".format(subTotal))

Notinha(nomeProduto, precoProduto, qtdProduto)