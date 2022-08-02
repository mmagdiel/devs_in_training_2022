'''
    Diseñar una función que retorne todas las permutaciones de una cadena de texto dada
'''
from itertools import permutations
def get_all_permutation_of_word(word):
    lista= [''.join(p) for p in permutations("cat")]
    return(lista)
