'''
    Diseñar un función que calcule el mayor valor de una lista L de N elementos.
'''
def maximum_list(lista): 
 Aux = 0
 for n in lista:
    if type(n) == type(bool(n)) or type(n) == str:
     print(aux)
    elif type(n) == type(dict()):
      print([]) 
    else:
        Aux = lista
        print(max(Aux))   
maximum_list([10,20,30,15])
 