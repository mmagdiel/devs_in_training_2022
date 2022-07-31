'''
    La seria de Fibonacci se define como: F_n = F_n-1 + F_n-2 y para n <= 1 F_n = 1.
    Calcule los número de fibonacci para un n dado.
'''
def get_fibonacci(number):
    if type(number)==type({"abc":35}):
        return []
    if number==str(number):
        return []
    if type(number)==type(float(number)):
        return []
    lista=[]
    dato1=1
    dato2=1
    for i in range(number):
        lista.append(dato1)
        dato3=dato1+dato2
        dato1=dato2
        dato2=dato3
    return(lista)