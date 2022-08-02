'''
    Diseñar una función de interes compuesto que reciba el capital a depositar, 
    la tasa de interés y la duración del depósito en semanas, 
    y calcular el capital total acumulado al final del período de tiempo especificado.
'''
def get_compound_interest(amount, rate, duration):
    list=[]
    if amount==str(amount) or rate==str(rate) or duration==str(duration) or type(amount)==type(list) or type(rate)==type(list) or type(duration)==type(type):
        return 0
    capital_total= amount*(1+rate)**duration
    return (round(capital_total,2))