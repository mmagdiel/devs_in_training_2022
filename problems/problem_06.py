'''
Escribir una función que recibe tres números y descubra si uno de ellos divide el producto de los otros dos
'''

def is_divide_product_of_the_other(n1, n2, n3):
    n1 = int(input("Ingrese el primer numero"))
    n2 = int(input("Ingrese el primer numero"))
    n3 = int(input("Ingrese el primer numero"))
    if n2 == 0:
        print("El divisor no puede ser cero")
    elif n3 == 0:
        print("El divisor no puede ser cero")
    else:
        print(n1/n2)
    
is_divide_product_of_the_other(3,5,5)