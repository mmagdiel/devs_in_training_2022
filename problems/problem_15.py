'''
    Diseñar una función que tome dos argumentos, una cantidad en dólares y un porcentaje de impuestos. 
    Retorne el monto del impuesto en centavos.
'''
from ntpath import realpath
from numbers import Real


def get_taxes_by_amount_and_rate():
    dolar=int
    porcentaje=input
    conversion=dolar*100
    total= (dolar*porcentaje)/100
    print("El ",(porcentaje), "porciento de ",(dolar), "es ",(total))
get_taxes_by_amount_and_rate()
