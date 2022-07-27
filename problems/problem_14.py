'''
    Diseñar una función que cuente el número de ocurrencias de cada letra en una palabra
leída como entrada. Por ejemplo, "Mortimer" contiene dos "m" , una "o" , dos "r" , una "i" ,
una "t" y una "e" .
'''
from itertools import count
from multiprocessing.sharedctypes import Value
from tkinter import END
from tracemalloc import start


word="mortimer"
def get_count_by_char(word):
   
    listWord1 = list(word)
   
    freq = listWord1.count("m",'o')
    

    print(freq,", m")
    

get_count_by_char(word)
