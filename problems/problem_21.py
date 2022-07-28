'''
    Diseñar una función que retorne todas las permutaciones de una cadena de texto dada
'''
def get_all_permutation_of_word(word):
    
    caracteres = list (word)
    permutaciones = []

    for c in caracteres:

        permutaciones.append (c)

    return permutaciones

