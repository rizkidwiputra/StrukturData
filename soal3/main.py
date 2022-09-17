print("\n=====> Antrian Bank <=====\n")

class Antrian:
    def __init__(self):
        self.panggil = 0
        self.antrian = 0
    
    def up_Panggil(self):
        if (self.panggil != self.antrian):
            self.panggil += 1

    def up_Antrian(self):
        self.antrian += 1

    def reset(self):
        self.panggil = 0
        self.antrian = 0
        
    def get_Panggil(self):
        return self.panggil

    def get_Antrian(self):
        return self.antrian

# ---> Implementasi ADT
bank = Antrian()
bank.up_Antrian()
bank.up_Antrian()
bank.up_Antrian()
bank.up_Panggil()
bank.up_Panggil()
bank.up_Panggil()
bank.up_Panggil()
bank.up_Antrian()
bank.up_Panggil()
bank.up_Antrian()
print(f"Jumlah Antrian : {bank.get_Antrian()} orang")
print(f"Jumlah Antrian yang terlayani : {bank.get_Panggil()} orang")