'''
    Diseñar una función que retorne los números del 1 hasta algún número
    ingresado por el usuario, sustituyendo los múltiplos de 3 por el palabro “Fizz” y, a su vez, los
    múltiplos de 5 por “Buzz”. Si al tiempo, son múltiplos de 3 y 5, escriba “FizzBuzz”.
'''
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

if __name__ == '__main__':
    sequence = '\n'.join(fizzbuzz(number) for number in range(15))
    return(sequence) 
