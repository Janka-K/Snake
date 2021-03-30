
from test import pohyb,nakresli_mapu

souradnice = [(0, 0), (1, 0), (2, 0)]
soucet_tahu = 0
pocet_tahu = 2
ovoce = [(2,3)]


while True:
    soucet_tahu +=1
    nakresli_mapu(souradnice,soucet_tahu,ovoce,pocet_tahu)
    svetova_strana = input(f"Zadej svetovou stranu ve forme s=sever,j=jih,v=vychod,z=zapad: ")
    pohyb(souradnice,svetova_strana)
    if soucet_tahu == pocet_tahu:
        soucet_tahu = 0

 




