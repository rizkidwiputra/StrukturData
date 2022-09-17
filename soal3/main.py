class Antrian:
    def __init__(self):
        self.panggil = 0
        self.antrian = 0
    
    def upPanggil(self):
        if not(self.panggil == self.antrian):
            self.panggil += 1

    def upAntrian(self):
        self.antrian += 1

    def reset(self):
        self.panggil = 0
        self.antrian = 0
        
    def getPanggil(self):
        return self.panggil

    def getAntrian(self):
        return self.antrian

bank = Antrian()
bank.upAntrian()
bank.upAntrian()
bank.upAntrian()
bank.upPanggil()
bank.upPanggil()
bank.upPanggil()
bank.upPanggil()
bank.upAntrian()
bank.upPanggil()
print("Jumlah Antrian", bank.getAntrian())
print("Jumlah Antrian yang telah terlayani", bank.getPanggil())