#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
def cuadrados_de_lista(numeros):
    cuadrados = []
    for numero in numeros:
        x = int(numero)**2
        cuadrados.append(x)
    return cuadrados

numeros = ["8", "5", "3", "4"]
resultado = cuadrados_de_lista(numeros)
print(resultado)