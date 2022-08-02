'''
    Diseñar una función para determinar los números primos iguales o menores que N
'''
def get_primes_less_or_equal_than(number):
    if number==str(number):
        return []
    if type(number)==type(1.2):
        return []
    list=[]
    contador=0
    for f in range(1,number+1):
        contador=0
        for c in range(1,number+1):
            if f%c==0:
                contador+=1
        if contador==2:
            list.append(f)
    return(list)
