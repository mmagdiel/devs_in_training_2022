'''
    Determinar si tres enteros a, b y c son o no una terna pitagórica, es decir, si es posible que:
    a^2 + b2 = c2 ó a^2 + c^2 = b^2 ó b^2 + c^2 = a2.
'''
def is_pythagorean_triple(number_1, number_2, number_3):
    list=[]
    if number_1==str(number_1) or number_2==str(number_2) or number_3==str(number_3) or type(number_1)==type(list) or type(number_2)==type(list) or type(number_3)==type(list):
        return False
    if number_1 < 0 or number_2 < 0 or number_3 < 0:
        number_1=abs(number_1)
        number_2=abs(number_2)
        number_3=abs(number_3)
    if number_1 > number_2 and number_1> number_3:
        if number_1**2 == number_2**2+number_3**2:
            return True
        else:
            return False
    elif number_2 > number_1 and number_2>number_3:
        if number_2**2 == number_1**2+number_3**2:
            return True
        else:
            return False
    else:
        if number_3**2 == number_2**2+number_1**2:
            return True
        else:
            return False
