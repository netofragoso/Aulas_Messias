
#with open("aula15.txt", "r", encoding="utf-8") as arquivo:
#    cont=arquivo.read()

with open("aula15.txt", "r", encoding="utf-8") as arquivo:
    x=0
    for linha in arquivo:
        x=x+1
        print(linha)
