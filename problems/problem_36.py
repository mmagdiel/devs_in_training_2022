'''
    Realizar un algoritmo que intercambie el valor de dos variables.
'''
def swap_vars(value_1, value_2):
    lista=[]
    aux=value_2
    value_2=value_1
    value_1=aux
    lista.append(value_1)
    lista.append(value_2)
    return lista
