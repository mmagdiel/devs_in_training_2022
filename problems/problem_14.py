'''
    Diseñar una función que cuente el número de ocurrencias de cada letra en una palabra
leída como entrada. Por ejemplo, "Mortimer" contiene dos "m" , una "o" , dos "r" , una "i" ,
una "t" y una "e" .
'''
def get_count_by_char(word):
    nombres = ['']
    resultado = list(map(lambda n: n.count('a'), nombres))
    print(resultado)
get_count_by_char("Proyecto") 