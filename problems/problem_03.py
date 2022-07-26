'''
    Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''
def mcm(number_1, number_2):
    i=1
    if  number_1 == str(number_1) or number_2 == str(number_2):
        return 0
    while True:
        if i%number_1==0 and i%number_2==0:
            mcm=i
            return mcm
            break
        i+=1