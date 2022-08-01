'''
    Diseñar una función de interes compuesto que reciba el capital a depositar, 
    la tasa de interés y la duración del depósito en semanas, 
    y calcular el capital total acumulado al final del período de tiempo especificado.
'''
def get_compound_interest(amount, rate, duration):
    if amount == str(amount) or rate == str(rate) or duration == str(duration) or type(amount) == type(list()):
        return(0)
    else:    
     pesos = amount
     interes = rate
     semana = duration
     
     x = (pesos * (1+interes/100) ** semana)
     
     return(int(x))
