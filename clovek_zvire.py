from kocka import Kocka
from enum import Enum


class ClovekZvire(Kocka):

    def __init__(self, jmeno, vaha, barva_tlapek,barva_pleti ,barva="nenastavena"):
        super().__init__(jmeno, vaha, barva_tlapek, barva_pleti, barva=barva)
        self.barva_pleti = barva_pleti

    def mluv(self):
        print("Huh")

    class Zbarveni(Enum):
        ZBARVENI_BILE = 1
        ZBARVENI_ZLUTE = 2
        ZBARVENI_CERNE = 3