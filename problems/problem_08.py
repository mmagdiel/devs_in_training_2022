'''
    Diseñar una función para determinar los números primos iguales o menores que N
'''


def get_primes_less_or_equal_than(number):
 cont = 0
numero = int(input("Ingrese un numero a evaluar: "))
for n in range(1, numero + 1):
    for d in range(1, n + 1):
        if n % d == 0:
            cont += 1
    if cont == 2:
        print("{}".format(n), end=" ")
    cont = 0
print("")

def get_primes_less_or_equal_than(number):
    number = 0
numero = int(input("Ingrese un numero a evaluar: "))
for n in range(1, numero + 1):
    for d in range(1, n + 1):
        if n % d == 0:
            number += 1
    if number == 2:
        print("{}".format(n), end=" ")
    number = 0
print("")
