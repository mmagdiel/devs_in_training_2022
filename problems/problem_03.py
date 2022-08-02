'''
    Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''
def mcm(number_1, number_2):
    if  number_1 == str(number_1) or number_2 == str(number_2):
        return 0
    if  type(number_1)== type(1.2) or type(number_2) == type(1.2):
        number_1=int(number_1)
        number_2=int(number_2)
    i=1
    while True:
        if i%number_1==0 and i%number_2==0:
            mcm=i
            return mcm
        i+=1
