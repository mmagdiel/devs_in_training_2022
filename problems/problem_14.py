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
    

  letra1 = counter["a"]
  letra2 = counter["b"]
  letra3 = counter["c"]
  letra4 = counter["d"]
  letra5 = counter["e"]
  letra6 = counter["f"]
  letra7 = counter["g"]
  letra8 = counter["h"]
  letra9 = counter["i"]
  letra10 = counter["j"]
  letra11 = counter["k"]
  letra12 = counter["l"]
  letra13 = counter["m"]
  letra14= counter["m"]
  letra15= counter["p"]
  letra16 = counter["ñ"]
  letra17 = counter["o"]
  letra18 = counter["r"]
  letra19 = counter["s"]
  letra20= counter["t"]
  letra21 = counter["v"]

  
    

get_count_by_char("mortimer")
