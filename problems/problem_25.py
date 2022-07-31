'''
    Determinar si tres enteros a, b y c son o no una terna pitagórica, es decir, si es posible que:
    a^2 + b2 = c2 ó a^2 + c^2 = b^2 ó b^2 + c^2 = a2.
'''
def is_pythagorean_triple(number_1, number_2, number_3):
   if number_1 == list(number_1) or number_2 == list(number_2) or number_3 == list(number_3) or number_1 == str(number_1) or number_2 == str(number_2) or number_3 == str(number_3):
    print(False) 
    if number_1**2 + number_2**2 == number_3**2 or number_3**2 + number_1**2==number_2**2 or number_2**2 + number_3**2 == number_1**2:
     print(True)
    else:
     print(False)   
is_pythagorean_triple(4,3,5)