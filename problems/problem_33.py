'''
    Diseñe un función que determine el porcentaje de varones y de mujeres que hay en un
    salón de clases. Dado la cantidad de varones y de mujeres
'''
def get_gender_percentage(males, females):
    
    if (males == int (males) and females == int (females)):
        
        total_alumnos = males + females
        porcentaje_m = total_alumnos * males / 100
        porcentaje_f = total_alumnos * females / 100
        
        return porcentaje_m , porcentaje_f