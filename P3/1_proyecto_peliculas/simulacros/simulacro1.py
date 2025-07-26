lista=[]

if len(lista)==0: 
    resp=True
    while resp:
        lista.append(input("Dame una palabra o frase: " ).upper())
        resp=input("¿Desea volver a ingresar otra palabra o frase? (SI/NO)").upper().strip()
        if resp=="NO":
            resp=False

    print(lista)
    
