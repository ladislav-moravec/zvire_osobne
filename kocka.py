from pes import Pes

class Kocka(Pes):

    def __init__(self, jmeno, vaha, barva_tlapek, barva="nenastavena"):
        super().__init__(jmeno,vaha, barva_tlapek, barva=barva)

    def mluv(self):
        print("Mnau")

