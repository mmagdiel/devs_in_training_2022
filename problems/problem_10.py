'''
    Diseñar una función calcular la longitud de la circunferencia y el área de un círculo de radio dado
'''
def get_lenght_and_area_circule(radio):
    if  radio == str(radio):
        return [0,0]
    if radio<0:
        return [0,0]
    longitud = 0
    area = 0
    lista=[]
    longitud = (2*3.1416)*radio
    longitudresul=round(longitud,4)
    area = 3.1416 * (radio**2)
    arearesul= round(area,4)
    lista.append(longitudresul)
    lista.append(arearesul)
    return(lista)
    
