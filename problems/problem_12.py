'''
    Diseñar una función que indique si una palabra leída del teclado es un palíndromo. 
    Un palíndromo es una palabra que se lee igual en ambos sentidos como “radar”.
'''
def is_palindrome(word):
    
    while True:
    
        palindromo = len(word)[::-1]

        if len(word) == palindromo:

            return palindromo
