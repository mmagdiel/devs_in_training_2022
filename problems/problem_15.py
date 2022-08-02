'''
    Diseñar una función que tome dos argumentos, una cantidad en dólares y un porcentaje de impuestos. 
    Retorne el monto del impuesto en centavos.
'''
from ntpath import realpath
from numbers import Real

def get_taxes_by_amount_and_rate(amount, rate):
    if rate==str(rate) or amount==str(amount):
        return 0
    conversion=(amount*100)
    total= (amount*rate)*100
    return total
