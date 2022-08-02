'''
    El sueldo neto de un vendedor se calcula como la suma de un sueldo básico 
    de 1 millón de pesos más el 12% del monto total vendido. 
    Diseñe una función que dado una lista de ventas determine el sueldo neto de un vendedor
'''
def get_salary(sales):
    
    sueldo_basico = int (1.000.000)

    for n in sales() :
        
        total_ventas = len(sales)
        total_comision = (total_ventas * 12) / 100
        sueldo_neto = total_comision + sueldo_basico
        
        return sueldo_neto
