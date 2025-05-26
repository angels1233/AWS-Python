def calculo_gorjeta(conta, gorjeta):
    
    val_gorjeta = conta*(gorjeta/100)

    return print("O valor da gorjeta de {:.1f}%: {:.2f}".format(gorjeta, val_gorjeta))

def entrada():
    
    conta = input("Digite o valor da conta: ")
    gorjeta = input("Digite a porcetagem da gorjeta: ")
    try:
        conta = float(conta)
        gorjeta = float(gorjeta)
    except:
        try:
            conta = conta.replace(",",".")
            gorjeta = gorjeta.replace(",",".")
            conta = float(conta)
            gorjeta = float(gorjeta)
        except:
            print("Valor da conta ou da gorjeta deve ser um número!")
            return entrada()
    
    calculo_gorjeta(conta, gorjeta)

entrada()