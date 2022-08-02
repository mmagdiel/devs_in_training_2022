'''
    Diseñar una función que dado un numero, sume los multiplo de 3 menores o igual a ese numero.
    Ejemplo: si n = 100 que sume la siguiente lista: 3, 6, 9, 12..., 99
'''
def sum_multiples_of_three(number):
    if  number == str(number):
        return 0
    elif number < 0: 
        i=-3
        cont=0
        while i >= number:
            cont=i+cont
            i=i-3
        return cont
    else:
        i=3
        cont=0
        while i <= number:
            cont=i+cont
            i=i+3
        return cont