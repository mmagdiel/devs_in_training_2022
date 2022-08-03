'''
    Diseñar una función que retorne, en orden inverso, cada múltiplo de 3 entre 1 y un número dado.
'''
def get_three_multiple_inverse_list(number):
    c=0 
    number=int(input("Introduzca el extremos superior: "))  
    print("Múltiplos de 2 y de 3 entre 1 y %i:"%number)  
    for i in range(1,number+1):  
     if i%2==0 and i%3==0:  
      c+=1  
      return(i)  
return(number)