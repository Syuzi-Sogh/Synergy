class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = 50


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage) # наследование от родителя происходит через super().

    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}  {self.capacity} пассажиров"

t1 = Autobus("Renal Logan", 180, 12)
print(t1.seating_capacity())