from mlb_data_scraper.pitcher import Pitcher


class Team:
    """Class containing data for an individual team"""

    def __init__(self, team_block, home_team: bool):
        self.team_block = team_block
        self.home_team = home_team
        self.team_name = None
        self.team_tricode = None
        self.pitcher = None
        self.batters = []
        self.set_vars()

    def set_team_name(self):
        self.team_name = self.team_block.a.get_text().strip()

    def set_team_tricode(self):
        self.team_tricode = self.team_block.a["data-tri-code"]

    def set_pitcher(self):
        self.pitcher = Pitcher(
            self.team_block.select(".starting-lineups__pitchers")[0], self.home_team
        )

    def set_vars(self):
        self.set_team_name()
        self.set_team_tricode()
        # self.set_pitcher()
