print("\n=====> Titik 2D <=====\n")

class titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def geser_horizontal(self,x):
        self.x += x

    def geser_vertikal(self, y):
        self.y += y
    
    def jarak(self, x2, y2):
        x = x2 - self.x
        y = y2 - self.y
        return (x**2 + y**2) ** (1/2)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

t1 = titik(2,3)
t2 = titik(4,5)
t1.geser_horizontal(-3)
t1.geser_vertikal(-7)
print(f"titik 1 ---> ({t1.getX()}, {t1.getY()})")
t2.geser_horizontal(15)
t2.geser_vertikal(9)
print(f"titik 2 ---> ({t2.getX()}, {t2.getY()})")
print(f"Jarak t1 dengan t2 ---> {t1.jarak(t2.getX(), t2.getY())}")