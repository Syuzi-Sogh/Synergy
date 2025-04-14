class Case(object):
    money = 0
    def __init__(self, m):
        self.money = m

    def top_up(self, m):
        self.money += m

    def count_1000(self):
        print("You have: ", self.money)

    def take_away(self, m):
        self.money -= m
        if self.money < 0:
            print("You don't have enough money!")
