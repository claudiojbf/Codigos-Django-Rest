import random

quantidade_numeros = int(input("Informe quantos numeros ira apostar de 6 a 15:"))

numeros = []

while quantidade_numeros < 6 or quantidade_numeros > 15: 
    quantidade_numeros = int(input("Informe quantos numeros ira apostar de 6 a 15:"))


for i in range(1000):
    numero_aleatorio = random.randrange(1,60)
    if numero_aleatorio not in numeros:
        numeros.append(numero_aleatorio)
        if len(numeros) == quantidade_numeros:
            break


print(numeros)