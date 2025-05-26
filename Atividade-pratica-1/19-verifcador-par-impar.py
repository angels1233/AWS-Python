def verif_paridade(numero):
    if numero%2 == 0:
        return "par"
    else:
        return "ímpar"
    
def main():   
    continuar = True
    pares = 0
    impares = 0

    while continuar:
        
        try:
            numero = int(input("Digite um número inteiro: "))
        except:
            print("O digito tem que ser um inteiro!")
            continue
        
        paridade = verif_paridade(numero)

        if paridade == 'par':
            print("{} é {}".format(numero,paridade))
            pares += 1
        else:
            print("{} é {}".format(numero,paridade))
            impares += 1

        verificar = input("Deseja verificar mais um numero? (S/N): ")
        
        match verificar.upper():
            case "S":
                continue
            case "N":
                continuar = False
                continue
    
    print("Você verificou----------\nNúmeros pares: {} \nNúmeros ímpares: {}".format(pares, impares))

main()