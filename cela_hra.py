#Napiš cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb, a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.

#Začínej se seznamem [(0, 0), (1, 0), (2, 0)].

from pohyb_vylepseny import pohyb
from nakresli_mapu import nakresli_mapu

souradnice = [(0, 0), (1, 0), (2, 0)]


while True:
  nakresli_mapu(souradnice)
  svetova_strana = input(f"Zadej svetovou stranu ve forme s=sever,j=jih,v=vychod,z=zapad: ")
  pohyb(souradnice,svetova_strana)



