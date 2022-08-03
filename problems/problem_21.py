 '''
    Diseñar una función que retorne todas las permutaciones de una cadena de texto dada
'''
def string_permutations(s, i, n): 
    if i==n: 
        print(''.join(s) )
    else: 
        for j in range(i,n): 
            s[i], s[j] = s[j], s[i] 
            string_permutations(s, i+1, n) 
            s[i], s[j] = s[j], s[i]  
a = "day"
x = len(a) 
s = list(a) 
return(a,x,s)