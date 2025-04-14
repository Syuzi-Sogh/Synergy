class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def Autobus(self):
        print(f"autobus name:{self.name} speed:{self.max_speed} mileage:{self.mileage} mileage:{self.mileage}")


t1 = Transport("Renaul Logan", 180, 12)
t1.Autobus()