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
    for i in range(1,number+1):
        contador=0
        for j in range(1,number+1):
            if i%j==0:
                contador+=1
        if contador==2:
            list.append(i)
    return(list)
