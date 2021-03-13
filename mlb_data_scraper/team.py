from mlb_data_scraper.batter import Batter
from mlb_data_scraper.pitcher import Pitcher


class Team:
    """Class containing data for an individual team"""

    def __init__(self, game_data, home_team: bool):
        self.game_data = game_data
        self.team_block = None
        self.pitcher_block = None
        self.home_team = home_team
        self.team_name = None
        self.team_tricode = None
        self.pitcher = None
        self.batters = [None] * 9
        self.set_vars()

    def set_team_block(self):
        if self.home_team:
            self.team_block = self.game_data.select(".starting-lineups__team-names")[0].select(
                ".starting-lineups__team-name--home"
            )[0]
        else:
            self.team_block = self.game_data.select(".starting-lineups__team-names")[0].select(
                ".starting-lineups__team-name--away"
            )[0]

    def set_pitcher_block(self):
        self.pitcher_block = self.game_data.select(".starting-lineups__pitchers")[0]

    def set_team_name(self):
        self.team_name = self.team_block.a.get_text().strip()

    def set_team_tricode(self):
        self.team_tricode = self.team_block.a["data-tri-code"]

    def set_pitcher(self):
        self.pitcher = Pitcher(self.pitcher_block, self.home_team)

    def set_batters(self):
        if self.home_team:
            lineup = self.game_data.find(
                class_="starting-lineups__team starting-lineups__team--home"
            ).select(".starting-lineups__player")
        else:
            lineup = self.game_data.find(
                class_="starting-lineups__team starting-lineups__team--away"
            ).select(".starting-lineups__player")

        if lineup:
            for i in range(len(lineup)):
                self.batters[i] = Batter(lineup[i], i + 1)

    def set_vars(self):
        self.set_team_block()
        self.set_pitcher_block()
        self.set_team_name()
        self.set_team_tricode()
        self.set_pitcher()
        self.set_batters()
