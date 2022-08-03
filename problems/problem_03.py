'''
Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''

def mcm(number_1, number_2):
    num1_org = []
    num2_org = []
    
    num1 = []
    num2 = []
    divisor = 2
    mcm = 1
    while num1!=1 or num2!=1:
        val = 0
        if num1%divisor == 0:
            num1 = num1/divisor
            val += 1
        if num2%divisor == 0:
            num2 = num2/divisor
            val += 1
        if val != 0:
            mcm = mcm*divisor
        else:
            divisor+=1
        return(f"El minimo comun multiplo entre {num1_org} y {num2_org} es {mcm}")
