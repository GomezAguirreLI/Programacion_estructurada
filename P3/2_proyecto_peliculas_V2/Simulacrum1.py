palabras = []
 
if palabras == []:
    opc=True
    while opc:   
        palabras.append(input("Ingresa: ").upper())
        resp=input("Otra? s/n").lower()
        if resp == "n":
            resp=False
print(palabras) 
