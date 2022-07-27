'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''

def get_lenght_and_area_circule(radio):
 pi = 3.1416
 if radio == str(radio):
   return([0,0])
 elif radio == 0 or radio < 0:
    return([0,0]) 
 else:  
  valor = radio / 2
  longitud = 2 * pi * valor
  numbAux= radio *2
  area = pi * numbAux
  return([area, longitud])

