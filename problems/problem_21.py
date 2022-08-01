'''
    Diseñar una función que retorne todas las permutaciones de una cadena de texto dada
'''
import itertools
from ntpath import join

def get_all_permutation_of_word(word):
 permutations = list(itertools.permutations(word))
 
 return(permutations)



