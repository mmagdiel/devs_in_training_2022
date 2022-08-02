'''
    Diseñar una función que cuente el número de ocurrencias de cada letra en una palabra
leída como entrada. Por ejemplo, "Mortimer" contiene dos "m" , una "o" , dos "r" , una "i" ,
una "t" y una "e" .
'''
from itertools import count
from multiprocessing.sharedctypes import Value
from tkinter import END
from tracemalloc import start
from typing import Counter



def get_count_by_char(word):
   
  counter = Counter(word)    
    

  print(counter["a"])
  print(counter["b"])
  print(counter["c"])
  print(counter["d"])
  print(counter["e"])
  print(counter["f"])
  print(counter["g"])
  print(counter["h"])
  print(counter["i"])
  print(counter["j"])
  print(counter["k"])
  print(counter["l"])
  print(counter["m"])
  print(counter["m"])
  print(counter["p"])
  print(counter["ñ"])
  print(counter["o"])
  print(counter["r"])
  print(counter["s"])
  print(counter["t"])
  print(counter["v"])
    

get_count_by_char("mortimer")
