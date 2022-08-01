'''
    Diseñar una función que calcule la superficie de un triángulo en función de la base y la altura
'''
def get_triangle_area(base, height):
    base = int(input("Input the base : "))
    height = int(input("Input the height : "))
    area = base*height/2
    return("area = ", area)

return(base,height,area)
