lista=[]

if len(lista)==0:
    resp=True
    while resp:
        lista.append(input("Dame una palabra: ").upper())
        resp=input("¿Desea solicitar otra frase? (Si/No)").lower().strip()
        if resp=="no":
            resp=False

print(lista)


