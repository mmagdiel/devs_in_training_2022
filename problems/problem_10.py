'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''
def get_lenght_and_area_circule(radio):
    if radio == str(radio) or radio < 0:
        return [0,0]
    longitud= 0
    lista= []
    longitud = 2 * radio * 3.1416
    area= 3.1416 * radio**2
    lista.append(longitud)
    lista.append(area)
    return lista