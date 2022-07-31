'''
    Diseñar un función que calcule el mayor valor de una lista L de N elementos.
'''
def maximum_list(lista):
    if type(lista)==type({"abc":123}):
        return 0
    if type(lista)==type(str(lista)):
        return 0
    for z in lista:
        if type(z)==bool:
            return 0
    for x in lista:
        n=x
        if type(n)==type({"abc":123}) or type(n)==type("a") or type(n)==type(None):
            return 0
    mayor = 0
    for el in lista:
        if mayor < el:
            mayor = el
        else:
            mayor = mayor
    return(mayor)
    
