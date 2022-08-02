'''
    Dados 3 números, deducir cuál es el central
'''
def get_center_number(number_1, number_2, number_3):
    
        if (number_1 > number_2 and number_1 < number_3) or (number_1 < number_2 and number_1 > number_3):
        
            return number_1
        
        elif (number_2 > number_1 and number_2 < number_3) or (number_2 < number_1 and number_2 > number_3):
        
            return number_2
        
        else:
        
            (number_3 > number_1 and number_3 < number_2) or (number_3 < number_1 and number_3 > number_2)
            
        return number_3
