import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


class Page:
    """Class containing data for full page"""

    def __init__(self, url):
        self.url = url
        self.page = None
        self.content = None
        self.games = []

    def download_page(self):
        """Downloads page from specified url"""
        self.page = requests.get(self.url)

    def set_page_content(self):
        """Extracts markup code from downloaded page"""
        self.content = BeautifulSoup(self.page.content, "html.parser")

    def get_games(self):
        """Return a list of games and all of their data"""
        self.games = [
            Game(game) for game in self.content.find_all(class_="starting-lineups__matchup")
        ]


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


class Team:
    """Class containing data for an individual team"""

    def __init__(self, team_block, home_team: bool):
        self.team_block = team_block
        self.home_team = home_team
        self.team_name = None
        self.team_tricode = None
        self.pitcher = None
        self.batters = []

    def set_team_name(self):
        self.team_name = self.team_block.a.get_text().strip()

    def get_team_name(self):
        return self.team_name

    def set_team_tricode(self):
        self.team_tricode = self.team_block.a.get_text().strip()

    def get_team_tricode(self):
        return self.team_tricode

    def get_pitcher(self):
        self.pitcher = Pitcher(
            self.team_block.select(".starting-lineups__pitchers")[0], self.home_team
        )

    def set_batters(self):
        if self.home_team:
            lineup = self.team_block.find(
                class_="starting-lineups__team starting-lineups__team--home"
            ).select(".starting-lineups__player")
        else:
            lineup = self.team_block.find(
                class_="starting-lineups__team starting-lineups__team--away"
            ).select(".starting-lineups__player")

        self.batters = [Batter(batter) for batter in lineup]

    def get_batter(self, position=None):
        if type(position) == int:
            return self.batters[position - 1]
        else:
            return self.batters


class Pitcher:
    """Class containing starting pitcher data"""

    def __init__(self, pitcher_block, home_team: bool):
        self.pitcher_block = pitcher_block
        self.home_team = home_team
        self.player_name = None
        self.player_id = None
        self.player_handedness = None

    def set_player_name(self):
        self.player_name = self.pitcher_block.select(".starting-lineups__pitcher-name")[
            0
        ].a.get_text()

    def get_player_name(self):
        return self.player_name

    def set_player_id(self):
        self.player_id = (
            self.pitcher_block.select(".starting-lineups__pitcher-name")[int(self.home_team)]
            .a["href"]
            .split("-")[2]
        )

    def get_player_id(self):
        return self.player_id

    def set_player_handedness(self):
        self.player_handedness = (
            self.pitcher_block.select(".starting-lineups__pitcher-pitch-hand")[int(self.home_team)]
            .get_text()
            .strip()
        )

    def get_player_handedness(self):
        return self.player_handedness


class Batter:
    """Class containing batter data"""

    def __init__(self, batter_block):
        self.batter_block = batter_block
        self.player_name = None
        self.player_id = None
        self.player_handedness = None
        self.player_position = None

    def set_player_name(self):
        self.player_name = " ".join(self.batter_block.get_text().split()[:-2])

    def get_player_name(self):
        return self.player_name

    def set_player_id(self):
        self.player_id = self.batter_block.a["href"].split("-")[-1]

    def get_player_id(self):
        return self.player_id

    def set_player_handedness(self):
        self.player_handedness = self.batter_block.get_text().split()[-2].strip("()")

    def get_player_handedness(self):
        return self.player_handedness

    def set_player_position(self):
        self.player_position = self.batter_block.get_text().split()[-1]

    def get_player_position(self):
        return self.player_position
