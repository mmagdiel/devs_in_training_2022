'''
    Diseñar una función que retorne los números del 1 hasta algún número
    ingresado por el usuario, sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, los
    múltiplos de 5 por “Buzz”. Si al tiempo, son múltiplos de 3 y 5, escriba “FizzBuzz”.
'''
def get_fizz_buzz(): 
    i = 1
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i)
        i= i + 1
get_fizz_buzz()
