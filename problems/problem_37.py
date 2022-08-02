'''
    La seria de Fibonacci se define como: F_n = F_n-1 + F_n-2 y para n <= 1 F_n = 1.
    Calcule los número de fibonacci para un n dado.
'''
def get_fibonacci(number):
    m=1
    f=0
    if number==1:
        return('0')
    elif number==2:
        return('0','1')
    elif type(number) == type(float()) or type(number) == type(str()) or type(number) == type(dict()): 
        return([])        
    else:
        lista=[]
    for i in range(number):
         total = m + f
         m=f
         f= total
         lista.append(total)
    return(lista)