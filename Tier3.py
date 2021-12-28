class Tier3:
    def __init__(self):
        self.vps = 0
        self.squares = 0

    def value_update(self):
        if self.squares == 0:
            self.vps = 0
        elif self.squares == 2:
            self.vps = 400
        elif self.squares == 3:
            self.vps = 500
        elif self.squares == 4:
            self.vps = 600
        elif self.squares == 5:
            self.vps = 700
        elif 6 <= self.squares <= 10:
            self.vps = 800
        elif 11 <= self.squares <= 20:
            self.vps = 900
        elif 21 <= self.squares <= 30:
            self.vps = 1000
        elif 31 <= self.squares <= 40:
            self.vps = 1100
        elif self.squares >= 41:
            self.vps = 1200


class Imperial(Tier3):
    def __init__(self):
        super().__init__()


class Continental(Tier3):
    def __init__(self):
        super().__init__()
