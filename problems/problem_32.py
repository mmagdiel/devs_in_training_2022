'''
    El sueldo neto de un vendedor se calcula como la suma de un sueldo básico 
    de 1 millón de pesos más el 12% del monto total vendido. 
    Diseñe una función que dado una lista de ventas determine el sueldo neto de un vendedor
'''
def get_salary(sales):
    sales = ["Lorem",7000000]
base = 1000000
if len(sales) == 0:
    print(base)
else:    
 for n in sales:
    num = n 
 if num == str(num):
         print(base)

 else:

  ventas = sum(sales)
  Comision = ventas * 0.12
  print(base + Comision)
get_salary([100000,200000,300000])    
