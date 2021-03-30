
# Doplň funkci pohyb tak, aby při pohybu umazala první bod ze seznamu souřadnic. 
# Výsledný seznam tak bude mít stejnou délku, jako před voláním.

#Doplň funkci pohyb tak, aby zamezila:
# 1) pohybu ven z mapy,
# 2) pohybu na políčko, které už v seznamu je.

#Vhodná výjimka pro tyto situace je ValueError('Game over').


def pohyb(souradnice,svetova_strana):
  """Funkce dostane jako argument seznam se souradnicemi 
  a svetovou stranu("j","s","v","z") a do seznamu ulozi
  novou souradnici posunutou podle svetove_strany
  Po vylepseni funkce pri pohybu umaze prvni bod ze seznamu souradnic, ktery dostava jako argument.
  Vysledny seznam ma stejnou delku jako pred volanim
  Funkce doplnena o zamezeni pohybu ven z mapy a pohybu na policko,ktere je jiz obsazene(je jiz v seznamu) ==>> pouzita
  vyjimka ValueError"""

  souradnice1 = 0
  souradnice2 = 0
  
  if svetova_strana.lower() == "v":
    souradnice1= (souradnice[-1][0])
    souradnice2= (souradnice[-1][1] + 1)
    souradnice.append((souradnice1,souradnice2))
  elif svetova_strana.lower() == "z":
    souradnice1 = (souradnice[-1][0])
    souradnice2 = (souradnice[-1][1] - 1)
    souradnice.append((souradnice1,souradnice2))
  elif svetova_strana.lower() == "j":
    souradnice1 = (souradnice[-1][0] + 1) 
    souradnice2 = (souradnice[-1][1])
    souradnice.append((souradnice1,souradnice2))
  elif svetova_strana.lower() == "s":
    souradnice1 = (souradnice[-1][0] - 1)
    souradnice2 = (souradnice[-1][1])
    souradnice.append((souradnice1,souradnice2))
  
  for i in souradnice[:-1]: 
      if i!= souradnice[-1]: 
          print(souradnice)
          del souradnice[0]
          print(souradnice)
      else:
        raise ValueError("Game over")

      if (souradnice[-1][0] < 0 or souradnice[-1][1] <0) or (souradnice[-1][0] > 10 or souradnice[-1][1] > 10):
        raise ValueError("Konec hry")

   

