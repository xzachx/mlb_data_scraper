from mlb_data_scraper.team import Team


class Game:
    """Class containing data for an individual game"""

    def __init__(self, game_data):
        self.game_data = game_data
        self.home_team = None
        self.away_team = None
        self.game_time = None
        self.park = None
        self.ppd = False

    def set_teams(self):
        """Extract code blocks for home and away teams"""
        self.home_team = Team(self.game_data, True)
        self.away_team = Team(self.game_data, False)

    def set_game_time(self):
        if self.game_data.select("time"):
            self.game_time = self.game_data.select("time")[0]["datetime"]

    def set_park(self):
        if self.game_data.find(class_="starting-lineups__game-location"):
            self.park = (
                self.game_data.find(class_="starting-lineups__game-location").get_text().strip()
            )

    def set_ppd(self):
        if self.game_data.find(
            class_="starting-lineups__game-state starting-lineups__game-state--postponed"
        ):
            self.ppd = True
        else:
            self.ppd = False

    def set_vars(self):
        self.set_teams()
        if self.home_team:
            self.home_team.set_vars()
        if self.away_team:
            self.away_team.set_vars()
        self.set_game_time()
        self.set_park()
        self.set_ppd()
