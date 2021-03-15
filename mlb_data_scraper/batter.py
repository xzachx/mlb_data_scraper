import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


class Batter:
    """Class containing batter data"""

    def __init__(self, batter_block, batting_num):
        self.batter_block = batter_block
        self.batting_num = batting_num
        self.player_name = None
        self.player_id = None
        self.player_handedness = None
        self.player_position = None
        self.batter_df = None

    def set_batter_block(self, batter_block):
        self.batter_block = batter_block

    def set_player_name(self):
        self.player_name = " ".join(self.batter_block.get_text().split()[:-2])

    def set_player_id(self):
        self.player_id = self.batter_block.a["href"].split("-")[-1]

    def set_player_handedness(self):
        self.player_handedness = self.batter_block.get_text().split()[-2].strip("()")

    def set_player_position(self):
        self.player_position = self.batter_block.get_text().split()[-1]

    def set_batter_df(self):
        if self.player_position != "P":
            batter_data = {
                "mlb_batter_name": self.player_name,
                "mlb_batter_id": self.player_id,
                "team_tricode": "",
                "game_time": "",
                "batting_num": self.batting_num,
                "position": self.player_position,
                "handedness": self.player_handedness,
                "park": "",
                "home_team": "",
                "mlb_opp_pitcher_name": "",
                "mlb_opp_pitcher_id": "",
                "mlb_opp_pitcher_handedness": "",
            }
            self.batter_df = pd.Series(batter_data).to_frame()

    def set_vars(self):
        self.set_player_name()
        self.set_player_id()
        self.set_player_handedness()
        self.set_player_position()
        self.set_batter_df()
