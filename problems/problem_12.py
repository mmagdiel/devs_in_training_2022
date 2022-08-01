
'''
    Diseñar una función que indique si una palabra leída del teclado es un palíndromo. 
    Un palíndromo es una palabra que se lee igual en ambos sentidos como “radar”.
'''
def is_palindrome(word):
    igual, aux = 0, 0
    texto = input("Ingrese la palabra que desea evaluar: ")
    for ind in reversed(range(0, len(texto))):
      if texto[ind].lower() == texto[aux].lower():
        igual += 1
      aux += 1
    if len(texto) == igual:
      return("El texto es palindromo!")
    else:
      return("El texto no es palindromo!")