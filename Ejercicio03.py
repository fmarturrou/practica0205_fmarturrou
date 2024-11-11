def area_circulo(pi, radio):
    return pi * radio**2
area_circulo(3.14, 5)

def volumen_cilindro(radio, altura):
    area = area_circulo(radio)
    return area * altura