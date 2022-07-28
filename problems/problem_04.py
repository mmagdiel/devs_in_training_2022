'''
    Diseñar una función que dado un numero, sume los multiplo de 3 menores o igual a ese numero.
    Ejemplo: si n = 100 que sume la siguiente lista: 3, 6, 9, 12..., 99
'''
def sum_multiples_of_three(number):
    
    if number == str (number):
        return 0
    elif number < 0:
        x=-3
        contador = 0
        while x >= number:
            contador= x + contador
            x=x - 3
        return contador
    else: 
        x=3
        contador = 0
        while x <= number:
            contador= x + contador
            x=x + 3
        return contador