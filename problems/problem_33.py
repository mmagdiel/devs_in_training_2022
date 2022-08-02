'''
    Diseñe un función que determine el porcentaje de varones y de mujeres que hay en un
    salón de clases. Dado la cantidad de varones y de mujeres
'''
def get_gender_percentage(males, females):
    if males==str(males)or females==str(females) or type(males)==list or type(females)==list or males<0 or females <0:
        return [0,0]
    lista=[]
    suma = males+females
    porciento_males= (males*100)/suma
    porciento_males2=round(porciento_males,2)
    porciento_females= (females*100)/suma
    porciento_females2=round(porciento_females,2)
    lista.append(porciento_males2)
    lista.append(porciento_females2)
    return lista