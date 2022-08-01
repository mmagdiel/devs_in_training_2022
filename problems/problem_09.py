
'''
    Diseñar una función que calcule la superficie de un triángulo en función de la base y la altura
'''
def get_triangle_area(base, height):
    base = int(input("Input the base : "))
    height = int(input("Input the height : "))
    area = base*height/2
    print("area = ", area)

get_triangle_area(7, 9)
