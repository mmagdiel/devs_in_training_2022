'''
    Diseñe un código para convertir una longitud dada en pies a centímetros.
    Considere que: 1 pie = 30.48 centímetros
'''
def convert_foot(unit):
    
    if unit == int (30.48):
        
        unit = (unit * 30.48) / 100
        
        return unit
