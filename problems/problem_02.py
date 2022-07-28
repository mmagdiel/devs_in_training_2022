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

    if number_1 == int (number_1 and number_2 == int (number_2)):

        number_1 , number_2 = number_2 , number_1 % number_2

        return number_1