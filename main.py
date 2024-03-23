def calcular(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

numeros = []
for i in range(10):
    numero = int(input("Ingresa el número {}: ".format(i + 1)))
    numeros.append(numero)
    
promedio = calcular(numeros)
print("El promedio es:", promedio)
