from zvire import Zvire

class Pes(Zvire):
    
    def __init__(self, jmeno, vaha, barva_tlapek, barva="nenastavena"):
        super().__init__(jmeno, vaha, barva=barva)
        self.barva_tlapek = barva_tlapek

    def __str__(self):
        return "{} {} {} {}".format(
            self.jmeno, self._vaha, self.barva, self.barva_tlapek
        )

    def mluv(self):
        print("Haf")
