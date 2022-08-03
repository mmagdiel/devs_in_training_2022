'''
    Diseñar una función que retorne los números del 1 hasta algún número
    ingresado por el usuario, sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, los
    múltiplos de 5 por “Buzz”. Si al tiempo, son múltiplos de 3 y 5, escriba “FizzBuzz”.
'''
from os import remove
import re
def get_fizz_buzz(number):

 number = "dfrr"
 lista1 =[]
 if type(number) == str:
    return([]) 
 else:    
  for fizzbuzz in range(1,number+1):
     if fizzbuzz <= 0:
        return([]) 
     elif fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        
         lista1.append("fizzbuzz")
     elif fizzbuzz % 3 == 0:
         lista1.append("fizz")
     elif fizzbuzz % 5 == 0:
         lista1.append("buzz")
     else:
         lista1.append(fizzbuzz)    
  resultado = (lista1)    
  return(resultado)     
