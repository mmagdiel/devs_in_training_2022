'''
    Escribir una función que recibe tres números y descubra si uno de ellos divide el producto de los otros dos.
'''
from unittest import result


def is_divide_product_of_the_other(number_1, number_2, number_3):
    if  number_1 == str(number_1) or  number_2 == str(number_2) or number_3 == str(number_3):
        print(False)
        
    elif number_1 == int(number_1) or number_2 == int(number_2) or number_3 == int(number_3) :
         result1 = number_2*number_3 
         result2= number_1*number_2
         result3 = number_3*number_1
    if number_1<0 and number_2<0 and number_3 <0:
        result1 = result1 *-1    
        result2 = result2 *-1  
        result3 = result3 *-1  
    elif number_1>0 and number_2>0 or number_3 >0:
         result1 = result1     
         result2 = result2   
         result3 = result3  
    if result1==number_1:
        return(True)
    elif result2 ==number_3:
        return(True)
    elif result3==number_2:
        return(True)
    else:
        return(False)


