'''
    Diseñe un función que determine el porcentaje de varones y de mujeres que hay en un
    salón de clases. Dado la cantidad de varones y de mujeres
'''
def get_gender_percentage(males, females):
    if males==str(males) or females==str(females):
        return [0,0]
    if type(males)==type(list()) or type(females)==type(list()):
        return [0,0]
    if males<0 or females<0:
        return [0,0]
    lista=[]
    porcentaje_males = 0
    porcentaje_females = 0
    total = males + females
    porcentaje_males = males * 100 / total
    porcentaje_females = females * 100 / total
    lista.append(round(porcentaje_males,2))
    lista.append(round(porcentaje_females,2))
    return (lista)