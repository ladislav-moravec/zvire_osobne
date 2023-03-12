class Zvire:

    def __init__(self, jmeno, vaha, barva="nenastavena"):
        self.vaha = vaha
        self.jmeno = jmeno
        self.barva = barva
        if self.vaha < 9:
            self.leta = True
        else:
            self.leta = False

    def nakrm(self, kolik):
        self.kolik = kolik
        self.vaha += self.kolik
        if self.vaha >= 9:
            self.leta = False

    def vypis(self):
        print("Zvíře: {}\nVáha: {}\nLétací: {}\n"
              .format(self.jmeno, self.vaha, self.leta))

    def set_vaha(self, vaha):
        self.vaha = vaha
        if self.vaha < 9:
            self.leta = True
        else:
            self.leta = False



