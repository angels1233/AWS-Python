import random
import string

def gerador(tamanho):
    #define a pool de caracteres a serem usados letras, números e pontuações
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    for _ in range(tamanho):
        senha += "".join(random.choice(caracteres))
    return senha

def pergunta():
    try:  
        tamanho = int(input("Qual tamanho da senha? "))
        if tamanho > 0:
            senha_teste = gerador(tamanho)
            return print("Senha: {}".format(senha_teste))
        else:
            print("Senha tem que ser maior que 0")
            return pergunta()
    except:
        print("O valor deve ser um número")
        return pergunta()

pergunta()

