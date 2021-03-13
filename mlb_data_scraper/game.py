from mlb_data_scraper.team import Team


class Game:
    """Class containing data for an individual game"""

    def __init__(self, game_data):
        self.game_data = game_data
        self.home_team = None
        self.away_team = None
        self.game_time = None
        self.park = None
        self.set_vars()

    def set_teams(self):
        """Extract code blocks for home and away teams"""
        # teams = self.game_data.select(".starting-lineups__team-names")[0]
        # self.home_team = Team(teams.select(".starting-lineups__team-name--home")[0], True)
        # self.away_team = Team(teams.select(".starting-lineups__team-name--away")[0], False)
        self.home_team = Team(self.game_data, True)
        self.away_team = Team(self.game_data, False)

    def set_game_time(self):
        if self.game_data.select("time"):
            self.game_time = self.game_data.select("time")[0]["datetime"]

    def set_park(self):
        if self.game_data.find(class_="starting-lineups__game-location"):
            self.park = self.game_data.find(class_="starting-lineups__game-location").get_text().strip()

    def set_vars(self):
        self.set_teams()
        self.set_game_time()
        self.set_park()
