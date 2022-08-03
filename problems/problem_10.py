
'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''
def get_lenght_and_area_circule(radio):
    import math
    diametro = int(input("Ingresa el diámetro: "))
    circunferencia = diametro * math.pi
    radio = diametro / 2
    return(f"La circunferencia es {circunferencia} y el radio es {radio}")
return(diametro,circunferencia,radio)

