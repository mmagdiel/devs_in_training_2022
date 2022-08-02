'''
    Diseñar una función que calcule la superficie de un triángulo en función de la base y la altura
'''
def get_triangle_area(base, height):
    if  base == str(base) or height==str(height):
        return 0
    if base<0 or height<0:
        return 0
    superficie=(base*height)/2
    return superficie
