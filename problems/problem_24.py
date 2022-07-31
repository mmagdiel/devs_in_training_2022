'''
    En una cierta empresa comercial, el sueldo mensual de los vendedores corresponde a la
    suma de un sueldo base, más una comisión que corresponde a un porcentaje de las
    ventas que el vendedor haya efectuado en el mes. Para cálculo de la comisión que le
    corresponde a cada vendedor por las ventas que realizó durante el mes, se usa la
    siguiente tabla:
    • Si las ventas fueron inferiores a $4.000.000 el vendedor no recibe comisión,
    • Si las ventas fueron iguales a $4.000.000 y menos de $10.000.000 la comisión es de un
    3% de las ventas, y
    • Si las ventas fueron iguales o superiores a $10.000.000 la comisión es de un 7% de las
    ventas
    Diseñe una función que ingrese el sueldo base del vendedor y el monto de las ventas que
    efectuó en el mes, calcule y muestre el sueldo mensual que le corresponde.
'''




def get_salary(base, sellers):
  comision = sellers * 0.3
  comision2 = sellers * 0.7  
  if base == str(base) or sellers == str(sellers) or base < 0 or sellers < 0:
    print(0)    
  elif sellers < 4000000:
    print(base)
  elif sellers > 4000000 and sellers<10000000: 
    print(int(base + comision)) 
  elif sellers > 10000000:
    print(int(base + comision2))  
get_salary(1000000,17000000)    
