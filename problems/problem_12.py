'''
    Diseñar una función que indique si una palabra leída del teclado es un palíndromo. 
    Un palíndromo es una palabra que se lee igual en ambos sentidos como “radar”.
'''
def is_palindrome(word):
    if str(word)==str(word)[::-1]:
        return True
    else:
        return False
