'''
    Diseñar una función que dado un numero, sume los multiplo de 3 menores o igual a ese numero.
    Ejemplo: si n = 100 que sume la siguiente lista: 3, 6, 9, 12..., 99
'''
from unittest import result


def sum_multiples_of_three(number):
 rest= []
 if number == str(number):
     return 0
 elif number < 0:
       suma = number *-1
       for n in range(0,suma+1):
        if n % 3 == 0:
         rest.append(n)
        fin = sum(rest)
       return(fin *-1)
 elif number>0:
  for n in range(0,number+1):
   if n % 3 == 0:
    rest.append(n)
  fin = sum(rest)  
  return(fin)

  

