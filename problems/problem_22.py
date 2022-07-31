'''
    Diseñar una función que reciba dos enteros positivos y devuelva True, si los números
    recibidos son primos relativos y devuelve False en caso contrario. Dos números son primos
    relativos si no tienen divisores comunes excepto la unidad
'''
def are_primes_relatives(number_1,number_2):
    if  number_1 == str(number_1) or number_2 == str(number_2):
        return False
    if number_1<0 or number_2<0:
        return False
    minimo=min(number_1,number_2)
    maximo=max(number_1,number_2)
    contador=2
    while contador<=minimo:
        if minimo%contador==0 and maximo%contador==0:
            return False
        contador=contador+1
    return True
    
