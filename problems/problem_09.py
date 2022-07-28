'''
    Diseñar una función que calcule la superficie de un triángulo en función de la base y la altura
'''
def get_triangle_area(base, height):
    
    if  base == int (base) or height == int (height):

        superficie = base * height / 2

        return superficie