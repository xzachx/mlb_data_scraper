from team import Team


class Game:
    """Class containing data for an individual game"""

    def __init__(self, data):
        self.data = data
        self.home_team = None
        self.away_team = None

    def set_teams(self):
        """Extract code blocks for home and away teams"""
        teams = self.data.select(".starting-lineups__team-names")[0]
        self.home_team = Team(teams.select(".starting-lineups__team-name--home")[0], True)
        self.away_team = Team(teams.select(".starting-lineups__team-name--away")[0], False)
