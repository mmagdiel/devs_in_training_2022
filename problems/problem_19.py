'''
    Diseñar una función de interes compuesto que reciba el capital a depositar, 
    la tasa de interés y la duración del depósito en semanas, 
    y calcular el capital total acumulado al final del período de tiempo especificado.
'''
def get_compound_interest(amount, rate, duration):
    pesos = float(input("Capital inicial: "))
    interes = float(input('Interes anual: '))
    semana = int(input('Cantidad de semana: '))
     
    x = (pesos * (1 + interes/100) ** semana)
     
    print('El capita total al cabo de %d semanas sera de %.2f' %(semana,x))
get_compound_interest(4,4,5)

