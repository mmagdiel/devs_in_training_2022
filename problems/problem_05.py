'''
    Escribir una función que lea cuatro números y retorne el mayor de los cuatro.
'''


def max_of_four_number(number_1, number_2, number_3, number_4):
    mayor = 0
for i in range (1, 5):
    print ('PROCESO ' + repr (i))
    un_numero = (input ('Ingresa el valor de un numero: '))
    try:
        un_numero=int(un_numero)
        if i==1 or mayor<un_numero:
            mayor=un_numero
    except:
        mayor=0
        break
    print ()
print ('Valor de mayor: ' + repr (mayor))