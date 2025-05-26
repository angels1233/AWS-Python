#Verfica se o ano digitado está correto
def valida_ano(ano):

    try:
        ano = int(ano)
        return ano
    except:
        print("Ano inválido!")
        return verif_ano_bissexto()


def verif_ano_bissexto():
    
    ano = valida_ano(input("Informe o ano que deseja saber se é bissexto: "))

    if ano%4 == 0:
        if ano%100 == 0:
            if ano%400 == 0:
                print("Ano de {} é bissexto".format(ano))
            else:
                print("Ano de {} não é bissexto".format(ano))    
        else:        
            print("Ano de {} é bissexto".format(ano))
    else:
        print("Ano de {} não é bissexto".format(ano))

verif_ano_bissexto()