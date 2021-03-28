#Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10, která určují sloupec a řádek) a vypíše je jako mapu:
#  mřížku 10×10, kde na políčka, která jsou v seznamu, napíše X, jinde tečku. Například:

#nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

#Jak na to?

#1)Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
#[['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
#2)Na příslušných místech nahraď tečky X-ky.
#3)Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.


#tabulka = []
#souradnice = (3,1)
#pocet_radku = 4
#pocet_sloupcu = 4
#
#for i in range(pocet_radku):
#  tabulka.append(["."] * pocet_sloupcu)
#
#tabulka[souradnice[0]][souradnice[1]] = "X"
#print(tabulka)

#for i in range(pocet_radku):
#  for j in tabulka[i]:  # tabulka[i] ==>> vyuziti predchoziho cyklu(pruchod cisel), k definovani indexu ==>>vybere v kazdem  pruchodu 
#    print(j, end = " ")                   cyklu jeden seznam seznamu (reprezenuje sloupce)
#  print()


def nakresli_mapu(souradnice): 
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
  
  for i in range(pocet_radku):
    for j in tabulka[i]:
      print(j, end = " ")
    print () # return neni potreba..pokud si funkci nevolame pres print(nakresli_mapu()),ale jen klasickym volanim ==>> none se nevypisuje



  
#nakresli_mapu([(1,1),(2,3),(3,3)])



