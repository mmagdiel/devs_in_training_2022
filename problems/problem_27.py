'''
    Diseñe un código para convertir una longitud dada en pies a centímetros.
    Considere que: 1 pie = 30.48 centímetros
'''
def convert_foot(unit):
    if unit == str(unit):    
     return(0)

    elif type(unit) == type(list()):
     return(0)
    elif unit < 0:
     return(0)
    else:
      return(unit * 30.48)


