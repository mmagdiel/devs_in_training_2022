'''
    Diseñe un código para convertir una longitud dada en pies a centímetros.
    Considere que: 1 pie = 30.48 centímetros
'''
def convert_foot(unit):
    if type(unit)==type(list()):
        return 0
    if unit==str(unit):
        return 0
    if unit<0:
        return 0
    longitud =0
    longitud = unit*30.48
    return round(longitud,4)
