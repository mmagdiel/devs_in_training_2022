'''
    Diseñar una función que indique si una palabra leída del teclado es un palíndromo. 
    Un palíndromo es una palabra que se lee igual en ambos sentidos como “radar”.
'''
def is_palindrome(word):
    frase = word.lower()
    frase = word.replace(' ', '')
    longitud = len(frase)
    if type(word) == type(int()):
        print(False)
    elif longitud % 2 == 0:
        izquierda = word[:longitud // 2]
        derecha = word[longitud // 2:]
    else:
        izquierda = word[:longitud // 2]
        derecha = word[longitud // 2 + 1:]
    
    print(izquierda == derecha[::-1])
is_palindrome("12321")    
    
