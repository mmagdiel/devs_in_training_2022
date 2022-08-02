'''
    Diseñar una función que cuente el número de ocurrencias de cada letra en una palabra
leída como entrada. Por ejemplo, "Mortimer" contiene dos "m" , una "o" , dos "r" , una "i" ,
una "t" y una "e" .
'''
def get_count_by_char(word):
    
    word == str (word)
    
    for n in word:

        if n in word:

            word[n] += 1

        else:

            word[n] = 1

    return n     
