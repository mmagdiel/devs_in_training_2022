'''
    Escribir una función que recibe tres números y descubra si uno de ellos divide el producto de los otros dos.
'''
def is_divide_product_of_the_other(number_1, number_2, number_3):
    #number_1=number_2 X number_3
    #number_2=number_3 X number_1
    #number_3=number_1 X number_2
    if  number_1 == str(number_1) or number_2 == str(number_2) or number_3 == str(number_3):
        return False
    if number_2*number_3==number_1:
        return True
    if number_1*number_2==number_3:
        return True
    if number_3*number_1==number_2:
        return True
    else:
        return False
