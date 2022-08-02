'''
    Diseñar una función que tome dos argumentos, una cantidad en dólares y un porcentaje de impuestos. 
    Retorne el monto del impuesto en centavos.
'''
def get_taxes_by_amount_and_rate(amount, rate):
    if  amount == str(amount) or rate==str(rate):
        return 0
    centavos_impuesto= amount* 100 
    result = centavos_impuesto * rate
    return int(result)
    
