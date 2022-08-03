'''
    Diseñar una función que calcule la superficie de un triángulo en función de la base y la altura
'''
def get_triangle_area(base, height):
   if base == str(base) or height == str(height):
        return(0)
   elif base < 0 or height < 0:
      return(0)    
   elif base == int(base) and height == int(height):
      return(int(base * height / 2))
   elif base == float(base) or height == float(height):
      return(float(base * height / 2))

    
 
    

