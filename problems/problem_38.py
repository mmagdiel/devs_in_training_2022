'''
    Dado un número en notación decimal convertirlo en notación romana, menor o igual al 3 mil
'''
def get_roman_notation(number):
    if type(number)==type(3.14) or number==None or number==True:
        return ""
    if number==str(number) or type(number)==type({"abc":100}):
        return ""
    if type(number)==type(list()):
        return ""
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numeral = ''
    i = 0
    while number > 0:
        for _ in range(number // numeros[i]):
            numeral += numerales[i]
            number -= numeros[i]
        i += 1
    return numeral
