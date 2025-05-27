'''
Crear un progama que calcule e imprima las tabla de muliplicar del 2

Requisitos:
2.-Sin funciones 



num=2
posicion=(1,2,3,4,5,6,7,8,9,10)

print(f"{num*posicion[0]}")
print(f"{num*posicion[1]}")
print(f"{num*posicion[2]}")
print(f"{num*posicion[3]}")
print(f"{num*posicion[4]}")
print(f"{num*posicion[5]}")
print(f"{num*posicion[6]}")
print(f"{num*posicion[7]}")
print(f"{num*posicion[8]}")
print(f"{num*posicion[9]}")
'''
'''
#version 1
num=int(input("Dame el numero de la tabla de multiplicar: "))
multi=num*1
print(f"{num}X1 = {multi}")
multi=num*2
print(f"{num}X2 = {multi}")
multi=num*3
print(f"{num}X3 = {multi}")
multi=num*4
print(f"{num}X4 = {multi}")
multi=num*5
print(f"{num}X5 = {multi}")
multi=num*6
print(f"{num}X6 = {multi}")
multi=num*7
print(f"{num}X7 = {multi}")
multi=num*8
print(f"{num}X8 = {multi}")
multi=num*9
print(f"{num}X9 = {multi}")
multi=num*10
print(f"{num}X10 = {multi}")

#version 2
num=int(input("Ingrese la tabla:"))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

i=1
num=int(input("Ingrese la tabla:"))
while i<=10:
  multi=num*i
  print(f"{num} x {i} = {multi}")      
  i+=1 
'''

def tablasMultiplicar(num):
    numero=num
    resp=""
    for i in range(1,11):
      resp+=(f"{numero} x {i} = {numero*i}")
    return resp
    
numero=int(input("Dame el numero de la tabla de multiplicar a calcular"))
print(f"Tabla de multiplicar del {numero}")
resultado=tablasMultiplicar(numero)
print(f"{resultado}")