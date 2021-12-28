class Tier1:
    def __init__(self):
        self.vps = 0
        self.squares = 0
        self.majority_bonus = 0
        self.minority_bonus = 0

    def value_update(self):
        if self.squares == 0:
            self.vps = 0
        elif self.squares == 2:
            self.vps = 200
            self.majority_bonus = 2000
            self.minority_bonus = 1000
        elif self.squares == 3:
            self.vps = 300
            self.majority_bonus = 3000
            self.minority_bonus = 1500
        elif self.squares == 4:
            self.vps = 400
            self.majority_bonus = 4000
            self.minority_bonus = 2000
        elif self.squares == 5:
            self.vps = 500
            self.majority_bonus = 5000
            self.minority_bonus = 2500
        elif 6 <= self.squares <= 10:
            self.vps = 600
            self.majority_bonus = 6000
            self.minority_bonus = 3000
        elif 11 <= self.squares <= 20:
            self.vps = 700
            self.majority_bonus = 7000
            self.minority_bonus = 3500
        elif 21 <= self.squares <= 30:
            self.vps = 800
            self.majority_bonus = 8000
            self.minority_bonus = 4000
        elif 31 <= self.squares <= 40:
            self.vps = 900
            self.majority_bonus = 9000
            self.minority_bonus = 4500
        elif self.squares >= 41:
            self.vps = 1000
            self.majority_bonus = 10000
            self.minority_bonus = 5000


class Tower(Tier1):
    def __init__(self):
        super().__init__()


class Luxor(Tier1):
    def __init__(self):
        super().__init__()