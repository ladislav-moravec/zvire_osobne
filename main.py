import enum

from zvire import Zvire
from pes import Pes
from kocka import Kocka
from clovek_zvire import ClovekZvire



kobra = Zvire("Kobra královská", 8, "černá")
kobra.vypis()
kobra.set_vaha(10)
kobra.vypis()
kobra.mluv()

try:
    kobra.nakrm(6)
    print("Stav létavisti: {}".format(kobra.leta))
except Exception as e:
    print(e)

gargamel = Pes("Laso Apsa", 10, "růžové", "bílý")
gargamel.vypis()
gargamel.set_vaha(8)
gargamel.vypis()
gargamel.mluv()
print(gargamel)

pepina = Kocka("Kocicak", 6, "fialové", "šedá")
print(pepina)
pepina.mluv()

zvirata = [
    gargamel,
    pepina,
    kobra,
    Kocka("Kocicaaak", 10, "zluta", "modré")
]

for zvire in zvirata:
    print(zvire)
    print(zvire.mluv())


