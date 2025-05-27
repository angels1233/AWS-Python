import csv

with open("Leitura-de-arquivos/dados.csv", "r", encoding= "utf8") as arquivo:
    conteudo = csv.reader(arquivo)
    

print(conteudo)