#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def calcular_media(numeros):
    suma = sum(int(numero) for numero in numeros)
    cuantos_numeros = len(numeros)
    media = suma / cuantos_numeros
    return media

numeros = ["8", "5", "3", "4"]
resultado = calcular_media(numeros)
print(resultado)