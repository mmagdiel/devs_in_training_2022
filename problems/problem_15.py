'''
    Diseñar una función que tome dos argumentos, una cantidad en dólares y un porcentaje de impuestos. 
    Retorne el monto del impuesto en centavos.
'''
from unittest import result


amount =200
rate = 0.1
def get_taxes_by_amount_and_rate(amount, rate):
    
  centavos = amount * 100
  result = centavos * rate

  print(int(result))

get_taxes_by_amount_and_rate(amount,rate)  