#Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z") a 
#přidá k seznamu poslední bod „posunutý“ v daném směru. Např.:

#souradnice = [(0, 0)]
#pohyb(souradnice, 'v')
#print(souradnice)         # → [(0, 0), (1, 0)]
#pohyb(souradnice, 'v')
#print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
#pohyb(souradnice, 'j')
#print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
#pohyb(souradnice, 's')
#print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
#Funkce by neměla nic vracet. Jen mění už existující seznam.


def pohyb(souradnice,svetova_strana):
  """Funkce dostane jako argument seznam se souradnicemi 
  a svetovou stranu("j","s","v","z") a do seznamu ulozi
  novou souradnici posunutou podle svetove_strany"""
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



