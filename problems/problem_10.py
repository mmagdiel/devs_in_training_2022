'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''

def get_lenght_and_area_circule(radio):
 pi = 3.1416
 if radio == str(radio):
   return [0,0]
 if radio == 0 or radio < 0:
    return [0,0]    
 valor = radio
 longitud = 2 * pi * radio
 numbAux= radio **2
 area = pi * numbAux
 longitud = round(longitud,4)
 area = round(area,4)
 return([longitud, area])

