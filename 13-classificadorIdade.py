

def classificador_idade():
    #Tratativa de erro caso o usuário digite uma letra
    try:
        idade = int(input("Digite a sua idade: "))
    except:
        print("Idade inválida!")
        return classificador_idade()
    
    if idade < 0: 
        #Tratando caso o a idade seja um número negativo
        print("Idade inválida!")
        return classificador_idade()
    elif idade >=0 and idade <= 12:
        print("Sua idade é {}, você é criança".format(idade))
    elif idade >=13 and idade <= 17:
        print("Sua idade é {}, você é adolescente".format(idade))
    elif idade >= 18 and idade <= 59:
        print("Sua idade é {}, você é adulto".format(idade))
    elif idade >= 60 and idade <= 130:
        print("Sua idade é {}, você é idoso".format(idade))
    else:
        print("Você é a pessoa mais velha do mundo!!!!!!\nIncriveis {} anos de idade!!".format(idade))
  
classificador_idade()
