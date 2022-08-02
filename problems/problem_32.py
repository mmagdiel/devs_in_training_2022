'''
    El sueldo neto de un vendedor se calcula como la suma de un sueldo básico 
    de 1 millón de pesos más el 12% del monto total vendido. 
    Diseñe una función que dado una lista de ventas determine el sueldo neto de un vendedor
'''
def get_salary(sales):
    sueldo_base=1000000
    suma=0
    if sales==str(sales):
        return sueldo_base
    for x in sales:
        if type(x)==str or x<0:
            return sueldo_base
    for el in sales:
        suma=suma+el
    comision= 12 * suma / 100
    return(comision+sueldo_base)