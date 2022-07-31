'''
    La seria de Fibonacci se define como: F_n = F_n-1 + F_n-2 y para n <= 1 F_n = 1.
    Calcule los número de fibonacci para un n dado.
'''
def get_fibonacci(number):
 a=1
 b=1
 
 if number==1:
    return('0')
 elif number==2:
     return('0','1')
 elif type(number) == type(float()): 
    return([])   
 elif type(number) == type(str()): 
    return([])    
 elif type(number) == type(dict()): 
    return([])    
 else:
    lista=[]
  
    for i in range(number-2):
         total = a + b
         b=a
         a= total
         lista.append("1","1",total)
    return(lista)    
