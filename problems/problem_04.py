
'''
    Diseñar una función que dado un numero, sume los multiplo de 3 menores o igual a ese numero.
    Ejemplo: si n = 100 que sume la siguiente lista: 3, 6, 9, 12..., 99
'''


def multiple(valor, multiple):

    return True if valor % multiple == 0 else False
 
multiples_3=[]
 
for i in range(100):
 
    if multiple(i, 3):
        multiples_3.append(i)
 
print ("Los multiples de 3 son:", multiples_3)