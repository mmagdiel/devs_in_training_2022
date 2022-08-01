'''
    Diseñe un código para convertir una longitud dada en pies a centímetros.
    Considere que: 1 pie = 30.48 centímetros
'''
def convert_foot(unit):
    if type(unit)==list or unit== str(unit) or unit <= 0:
        return 0
    total=(unit*30.48)/1
    total2=round(total,3)
    return total2
