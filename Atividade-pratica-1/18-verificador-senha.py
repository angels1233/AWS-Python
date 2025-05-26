import getpass

def verificador():

    senha = getpass.getpass("Digite uma senha para verificação: ")

    if len(senha) < 8:
        print("Senha de ter no mínimo 8 digitos")
        return verificador()
    elif any(digito.isdigit() for digito in senha):
        print("Senha forte!")
    else:
        print("Senha fraca! ")
        return verificador()
    
verificador()