'''
    Diseñar una función que tome dos argumentos, una cantidad en dólares y un porcentaje de impuestos. 
    Retorne el monto del impuesto en centavos.
'''
def get_taxes_by_amount_and_rate(amount, rate):
    
    if (amount == int (amount) and rate == int (rate)):

        rate = rate / 100

        return rate 
