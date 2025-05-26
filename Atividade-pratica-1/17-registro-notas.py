
#Função de tratamento se continua ou não adicionando notas com retorno boleano
def pergunta():
    resposta = input("Deseja adicionar mais notas? (S/N): ")
    try:
        resposta = resposta.upper()
        if resposta == "S":
            return True
        elif resposta == "N":
            return False
        else:
            print("Resposta inválida!")
            return pergunta()
    except:
        print("Resposta deve ser S ou N!")
        return pergunta()

#Função que realiza o calculo da média
def  calculo_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    
    media = soma/len(notas)
    return media

#Função de registro de notas e tratamentos das execções
def registro_notas():
    notas = []
    adicionar = True

    while adicionar:
        
        nota = input("Adicione a nota do aluno entre 0 e 10: ")
        
        try:
            #tramanento de notas fora da range de 0 a 10
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
                adicionar = pergunta()
            else:
                print("Nota deve estar entre 0 e 10!")
                adicionar = pergunta()   
        except:
            try:
                #Tratamento de número com , passando pra .
                nota = nota.replace(",",".")
                nota = float(nota)
                notas.append(nota)
                adicionar = pergunta()
            except:
                print("Nota inválida")
                adicionar = pergunta()

    print("A média da turma é {:.2f} ".format(calculo_media(notas)))

registro_notas()
