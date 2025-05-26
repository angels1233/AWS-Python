#validador de dados e conversor pra float
def validador(num):
    try:
        num = float(num)
        return num
    except:
        num = num.replace(",",".")
        try:
            num = float(num)
            return num
        except:
            print("Altura ou Peso inválidos!")
            return calculo_imc()
        
def calculo_imc():

    peso = validador(input("Informe seu peso: "))
    altura = validador(input("Informe sua altura: "))

    #calculo do IMC
    imc = peso / (altura**2)
    
    match imc:
        case imc if imc < 18.5:
            print("Você está abaixo do peso e seu IMC é: {:.1f}".format(imc))
        case imc if 18.5 <= imc <=24.9:
            print("Você está com do peso normal e seu IMC é: {:.1f}".format(imc))
        case imc if  25.0 <= imc <= 29.9:
            print("Você está com sobrepeso e seu IMC é: {:.1f}".format(imc))
        case imc if 30 <= imc <= 39.9:
            print("Você está obeso e seu IMC é: {:.1f}".format(imc))
        case imc if imc > 40:
            print("Você está com obesidade grave e seu IMC é: {:.1f}".format(imc))

calculo_imc()