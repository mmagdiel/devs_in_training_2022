'''
    Diseñar una función que reciba y retorne una serie de números distintos de cero. 
    La función debe terminar con un valor cero que no se debe retornar, debe el número de valores leídos.
'''
ddef show_any_number_distinc_zero(listTmp):
    listadoY = []
    for item in listTmp:
        if isinstance(item,str):
            print('Tipo dato strim')
        else:
            if item > 0:
               listadoY.append(item)
            else:
                print('Este es cero', item)
                pass
            pass
        pass
    return listadoY,len(listTmp)

#listaNumeros = [0,0]
listaNumeros = ['3','7',0]
listdoNum, cantidadRecor = show_any_number_distinc_zero( listaNumeros )
print('Numeros leidos:', cantidadRecor)
print('Numeros retornados != 0:', listdoNum)
