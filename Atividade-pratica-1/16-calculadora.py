#Função que valida os número digitados
def val_num(num):
    try:
        num = int(num)
        return num
    except:
        print("Digite um número!")
        return calculadora()

    
def calculadora():
    val_operacao = True
    num1 = val_num(input("Informe o primeiro valor: "))
    num2 = val_num(input("Informe o segundo valor: "))

    #Estrutura de repetição para a escolha da operação
    while val_operacao:
        
        print("Operações disponíveis.\n + (Adição)\n - (Subtração)\n * (Multiplicação)\n / (Divisão)")
        operacao = input("Informe a operação desejada: ")
        
        #Estrutura de match para associar as opção com o sinal e a palavra
        match (operacao.upper()):
            case "+" | "ADIÇÃO":
                resultado = num1 + num2
                print("A soma de {} + {} = {}".format(num1,num2, resultado))
                val_operacao = False

            case "-" | "SUBTRAÇÃO":
                resultado = num1 - num2
                print("A subtração de {} - {} = {}".format(num1,num2, resultado))
                val_operacao = False
                
            case "*" | "MULTIPLICAÇÃO":
                resultado = num1 * num2
                print("A multiplicação de {} x {} = {}".format(num1,num2, resultado))
                val_operacao = False

            case "/" | "DIVISÃO":
                #Tratamento de divisão por 0
                try:
                    resultado = num1 / num2
                    print("A divisão de {} / {} = {}".format(num1,num2, resultado))
                    val_operacao = False
                except:
                    print("Impossivel dividir por 0\nPorfavor escolha novamente!")
                    val_operacao = True
                
            case _:
                print("Operação inválida!\nEscolha novamente")
                val_operacao = True              


calculadora()