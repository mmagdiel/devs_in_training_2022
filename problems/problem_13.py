'''
    Diseñar una función número determine si este es par
'''
def is_even(number):
    if  number == str(number):
        return False
    if number%2==0:
        return True
    else:
        return False
