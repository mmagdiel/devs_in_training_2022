'''
    Escribir una función para determinar el máximo común divisor de dos números enteros por el algoritmo de Euclides:
    - Dividir el mayor de los dos enteros positivos por el
    más pequeño.
    - A continuación dividir el divisor por el resto.
    - Continuar el proceso de dividir el último divisor por
    el último resto hasta que la división sea exacta.
    - El último divisor es el mcd.
'''
def MCD(number_1, number_2):     
    if number_1 == str(number_1) or number_2 == str(number_2):
        return 0
    while True: 
        residuo = number_1 % number_2
        if residuo == 0:
            return number_2
        else:
            number_1 = number_2
            number_2 = residuo