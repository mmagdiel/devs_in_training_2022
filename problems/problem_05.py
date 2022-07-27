'''
    Escribir una función que lea cuatro números y retorne el mayor de los cuatro.
'''
def max_of_four_number(number_1, number_2, number_3, number_4):
    if number_2 > number_1 and number_2 > number_3 and number_2 > number_4:
      print(number_2)
    elif  number_1 > number_2 and number_1 > number_3 and number_1 > number_4:
        print(number_1)
    elif number_3 > number_1 and number_3 > number_2 and number_3 > number_4:
        print(number_3)
    else:
       print(number_4)        




max_of_four_number(1,2,3,4)        