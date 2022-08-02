'''
    Determinar si tres enteros a, b y c son o no una terna pitagórica, es decir, si es posible que:
    a^2 + b2 = c2 ó a^2 + c^2 = b^2 ó b^2 + c^2 = a2.
'''
def is_pythagorean_triple(number_1, number_2, number_3):
    
    if number_1 ** 2 == number_2 ** 2 + number_3 ** 2 and number_2 ** 2 == number_1 ** 2 + number_3 ** 2 and number_3 ** 2 == number_1 ** 2 + number_2 ** 2:
        
        return (is_pythagorean_triple(number_1, number_2, number_3))
        
    else:
    
        print ("Los numeros:", number_1, number_2 , number_3 " no son una terna pitagorica")

