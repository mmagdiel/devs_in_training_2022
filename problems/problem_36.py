'''
    Realizar un algoritmo que intercambie el valor de dos variables.
'''
def swap_vars(value_1, value_2):
    list = []
    aux = value_1
    value_1 = value_2
    value_2 = aux
    list.append(value_1)
    list.append(value_2)
    return (list)
