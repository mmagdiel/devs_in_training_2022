'''
    Diseñar una función número determine si este es par
'''
def is_even(number):
    
    if number == str(number):
        return "false"
    if number % 2 == 0:
        return "true"
    else:
        return "false"
