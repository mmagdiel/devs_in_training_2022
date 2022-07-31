'''
    Diseñe un función que determine el porcentaje de varones y de mujeres que hay en un
    salón de clases. Dado la cantidad de varones y de mujeres
'''
def get_gender_percentage(males, females):
    total = males +females
    print(total / males)

get_gender_percentage(66.66, 33.33)    