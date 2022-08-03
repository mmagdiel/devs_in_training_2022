'''
    Una institución benéfica ha recibido tres donaciones en soles, dólares y marcos. La
    donación será repartida en tres rubros: 55% para la implementación de un centro de salud,
    35% para un comedor de niños y el resto para gastos administrativos. Diseñe un algoritmo
    que determine el monto en pesos que le corresponden a cada rubro. Considere que: 1
    dólar = 3.52 soles, 1 dólar = 2.08 marcos, 1 dólar = 2,15 pesos.
'''
def get_pesos_donations(suns, dolars, marks):
   
    if suns == str(suns) or dolars == str(suns) or marks == str(marks):
        return([0,0])
    elif type(suns) == type(list())or type(dolars) == type(list()) or type(marks) == type(list()):
        return([0,0])
    elif suns < 0 or dolars < 0 or marks < 0:
        return([0,0])    
    else:  
      dolarSoles = suns / 3.52
      dolarMarks = marks / 2.08
      totalDolars = dolars + dolarMarks + dolarSoles
      pesos = totalDolars * 2.15
      rubro1 = pesos * 0.55
      rubro2 = pesos * 0.35
      resultado = [round(rubro1,4),round(rubro2,4)]         
      return(resultado)
    
 
