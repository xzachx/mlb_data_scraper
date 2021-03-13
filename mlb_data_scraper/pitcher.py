class Pitcher:
    """Class containing starting pitcher data"""

    def __init__(self, pitcher_block=None, home_team=None):
        self.pitcher_block = pitcher_block
        self.home_team = home_team
        self.player_name = None
        self.player_id = None
        self.player_handedness = None

    def set_pitcher_block(self, pitcher_block):
        self.pitcher_block = pitcher_block

    def set_home_team(self, home_team: bool):
        self.home_team = home_team

    def set_player_name(self):
        self.player_name = self.pitcher_block.select(".starting-lineups__pitcher-name")[
            int(self.home_team)
        ].a.get_text()

    def set_player_id(self):
        self.player_id = (
            self.pitcher_block.select(".starting-lineups__pitcher-name")[int(self.home_team)]
            .a["href"]
            .split("-")[2]
        )

    def set_player_handedness(self):
        self.player_handedness = (
            self.pitcher_block.select(".starting-lineups__pitcher-pitch-hand")[int(self.home_team)]
            .get_text()
            .strip()
        )

    def set_vars(self):
        self.set_player_name()
        self.set_player_id()
        self.set_player_handedness()
