#Přidej do hry hadí potravu. Tady jsou pravidla pro vegetariánského hada, ale můžeš si je změnit podle chuti:

#Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to, cos přidala v projektu 3), 
# a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.

from random import randrange,randint

def nakresli_mapu(souradnice,pocet_tahu,ovoce,soucet_tahu): 
  """Funkce vykresli tabulku z tecek
  delka tabulky je urcena poctem radku a sloupcu
  a na jeden bod podle zadanych souradnic vykresli
  "X" """
  tabulka = []
  pocet_radku = 10
  pocet_sloupcu = 10

  for i in range(pocet_radku):
      tabulka.append(["."] * pocet_sloupcu)
  
  for i in souradnice:
      tabulka[i[0]][i[1]] = "X"

  for i in ovoce:
    tabulka[i[0]][i[1]] = "?"


  obsahuje_ovoce = False
  
  for i in range(pocet_radku):
    if "?" in tabulka[i]:
      obsahuje_ovoce = True
      break

  if obsahuje_ovoce == False:
    ovoce_souradnice1 = randrange(pocet_radku)
    ovoce_souradnice2 = randrange(pocet_sloupcu)
    del ovoce[0]
    ovoce.append((ovoce_souradnice1,ovoce_souradnice2))

  for j in ovoce:
      tabulka[j[0]][j[1]] = "?"

  if pocet_tahu == soucet_tahu:
      ovoce_souradnice1 = randrange(pocet_radku)
      ovoce_souradnice2 = randrange(pocet_sloupcu)
      ovoce.append((ovoce_souradnice1,ovoce_souradnice2))
      

  for j in ovoce:
    tabulka[j[0]][j[1]] = "?"



  for i in range(pocet_radku):
      for j in tabulka[i]:
        print(j, end = " ")
      print ()



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


#souradnice = [(0, 0), (1, 0), (2, 0)]

#nakresli_mapu([(0, 0), (1, 0), (2, 0)])

## Aktualne je potreba zajistit:

# 1) Nesmazani hadiho ocasu (funkce pohyb) pote co sezere ovoce 
# (oznaceno "?")

# 2) Pokud na mape zrovna neni zadne ovoce ("?"), vyroste na mape ovoce ==>> splneno castecne // potreba osetrit dopady, jakmile
# po 30ti tazich pribyde do seznamu ovoce nove (v miste,kde zrovna neni had "X")

# 3) Po kazdych 30ti tazich na mape vyroste ovoce nove == vyreseno
