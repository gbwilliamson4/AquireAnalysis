class Players:
    def __init__(self, player_name, key):
        self.player_name = player_name
        # print(self.player_name)
        self.key = key

        # Company holdings. Leave self.holdings for testing purposes so it doesnt all break.
        self.holdings = 0

        # Tier 1 holdings
        self.tower_holdings = 0
        self.luxor_holdings = 0

        # Tier 2 holdings
        self.american_holdings = 0
        self.festival_holdings = 0
        self.worldwide_holdings = 0

        # Tier 3 holdings
        self.imperial_holdings = 0
        self.continental_holdings = 0
