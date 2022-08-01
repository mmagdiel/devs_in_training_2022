'''
    Diseñar una función que retorne los números del 1 hasta algún número
    ingresado por el usuario, sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, los
    múltiplos de 5 por “Buzz”. Si al tiempo, son múltiplos de 3 y 5, escriba “FizzBuzz”.
'''
def get_fizz_buzz(number):
    if number==str(number) or number<0:
        return []
    list=[]
    for i in range(1,number+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
            i= i + 1
    return(list)
