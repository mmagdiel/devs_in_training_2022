'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''
def get_lenght_and_area_circule(radio):
    
    if radio == int (radio):

        longitud = (2*3.1416) * radio

        area = longitud * radio 

        return longitud , area 

