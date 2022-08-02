'''
    Dado un número en notación decimal convertirlo en notación romana, menor o igual al 3 mil
'''
from math import trunc


def get_roman_notation(number):
    
    if number == int (number):

        millar = trunc(number/1000) /10 
        centena = trunc(number/100) /10
        decena = trunc(number/10) /10
        unidades = trunc(number/1) / 10

    if (millar > 3.000):

        print ("El numero no se puede convertir")

    else:

        switch : (millar)

        1: print ("M", end= "")
        
        2: print ("MM", end= "")

        3: print ("MMM", end = "")

        switch : (centena)

        1: print ("C", end = "")

        2: print ("CC", end = "")

        3: print ("CCC", end = "")

        4: print ("CD", end = "")

        5: print ("D", end = "")

        6: print ("DC", end = "")

        7: print ("DCC", end = "")

        8: print ("DCCC", end = "")

        9: print ("CM", end = "")

        switch : (decena)

        1: print ("X", end = "")

        2: print ("XX", end = "")

        3: print ("XXX", end = "")

        4: print ("XL", end = "")

        5: print ("L", end = "")

        6: print ("LX", end = "")

        7: print ("LXX", end = "")

        8: print ("LXXX", end = "")

        9: print ("XC", end = "")

        switch : (unidades)

        1: print ("I", end = "")

        2: print ("II", end = "")

        3: print ("III", end = "")

        4: print ("IV", end = "")

        5: print ("V", end = "")

        6: print ("VI", end = "")

        7: print ("VII", end = "")

        8: print ("VIII", end = "")

        9: print ("IX", end = "")

    return millar , centena , decena , unidades
