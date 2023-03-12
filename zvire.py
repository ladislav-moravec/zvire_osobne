class Zvire:

    def __init__(self, jmeno, vaha, barva="nenastavena"):
        self._vaha = vaha
        self.jmeno = jmeno
        self.barva = barva
        if self._vaha < 9:
            self.leta = True
        else:
            self.leta = False

    def nakrm(self, kolik):
        if kolik > 5:
            raise Exception("Nemuze snist vice než 5 kg najednou.")
        self._vaha += self.kolik
        if self._vaha >= 9:
            self.leta = False

    def vypis(self):
        print("Zvíře: {}\nVáha: {}\nLétací: {}\n"
              .format(self.jmeno, self._vaha, self.leta))

    def set_vaha(self, vaha):
        self._vaha = vaha
        if self._vaha < 9:
            self.leta = True
        else:
            self.leta = False

    def mluv(self):
        print("...")