

class Pitcher:
    """Class containing starting pitcher data"""

    def __init__(self, pitcher_block, home_team: bool):
        self.pitcher_block = pitcher_block
        self.home_team = home_team
        self.player_name = None
        self.player_id = None
        self.player_handedness = None
        self.set_vars()

    def set_player_name(self):
        self.player_name = self.pitcher_block.select(".starting-lineups__pitcher-name")[
            0
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
