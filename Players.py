class Players:
    def __init__(self, player_name):
        self.player_name = player_name
        # print(self.player_name)
        self.key = 0

        # Company holdings. Leave self.holdings for testing purposes so it doesnt all break.
        self.holdings = 0

        self.tower_holdings = 0
        self.american_holdings = 0
        self.imperial_holdings = 0

