class Turtle(object):
    x = 0
    y = 0
    s = 0
    def __init__(self, x_, y_, s_):
        self.x = x_
        self.y = y_
        self.s = s_

    def go_up(self):
        self.y = self.y + self.s

    def go_down(self):
        self.y = self.y - self.s

    def go_left(self):
        self.x = self.x - self.s

    def go_right(self):
        self.x = self.x + self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        self.s -= 1
        if self.s <= 0:
            print("Wrong")

    def count_moves(self, x2, y2):
        new_x = abs(x2 - self.x)
        new_y = abs(y2 - self.y)
        moves_by_x = (new_x + self.s - 1) // self.s
        moves_by_y = (new_y + self.s - 1) // self.s
        return moves_by_x + moves_by_y
