'''
    Una institución benéfica ha recibido tres donaciones en soles, dólares y marcos. La
    donación será repartida en tres rubros: 55% para la implementación de un centro de salud,
    35% para un comedor de niños y el resto para gastos administrativos. Diseñe un algoritmo
    que determine el monto en pesos que le corresponden a cada rubro. Considere que: 1
    dólar = 3.52 soles, 1 dólar = 2.08 marcos, 1 dólar = 2,15 pesos.
'''
def get_pesos_donations(suns, dolars, marks):
    lista=[]
    if type(suns)==type(list()) or type(dolars)==type(list()) or type(marks)==type(list()):
        return [0,0]
    if suns==str(suns) or dolars==str(dolars) or marks==str(marks):
        return [0,0]
    if suns<0 or dolars<0 or marks<0:
        return [0,0]
    conversion_suns= suns / 3.52
    conversion_marks= marks / 2.08
    dolares_totales = conversion_suns + conversion_marks + dolars
    pesos = dolares_totales * 2.15
    centro_salud = (pesos * 55) / 100
    comedor = (pesos * 35) / 100
    adminstracion = (pesos * 10) / 100
    lista.append(round(centro_salud,4))
    lista.append(comedor)
    return lista
