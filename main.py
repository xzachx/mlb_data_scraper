import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup


def get_page(url):
    """Downloads page from specified url"""
    page = requests.get(url)
    return page


def get_page_content(page):
    """Extracts markup code from downloaded page"""
    content = BeautifulSoup(page.content, "html.parser")
    return content


def get_games(content):
    """Return a list of games and all of their data"""
    games = content.find_all(class_="starting-lineups__matchup")
    return games


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
        self.batters = None

    def set_team_name(self):
        self.team_name = self.team_block.a.get_text().strip()

    def get_team_name(self):
        return self.team_name

    def set_team_tricode(self):
        self.team_tricode = self.team_block.a.get_text().strip()

    def get_team_tricode(self):
        return self.team_tricode

    def get_pitcher(self):
        # TODO: Define get_pitcher() method
        pass

    def get_batters(self):
        # TODO: Define get_batters() method
        pass


class Pitcher:
    """Class containing starting pitcher data"""

    def __init__(self, pitcher_block):
        self.pitcher_block = pitcher_block
        self.player_name = None
        self.player_id = None
        self.player_handedness = None

    def set_player_name(self):
        # TODO: Define set_player_name() method
        pass

    def get_player_name(self):
        return self.player_name

    def set_player_id(self):
        # TODO: Define set_player_id() method
        pass

    def get_player_id(self):
        return self.player_id


class Batter:
    """Class containing batter data"""

    def __init__(self, batter_block):
        self.batter_block = batter_block
        self.player_name = None
        self.player_id = None
        self.player_handedness = None

    def set_player_name(self):
        # TODO: Define set_player_name() method
        pass

    def get_player_name(self):
        return self.player_name

    def set_player_id(self):
        # TODO: Define set_player_id() method
        pass

    def get_player_id(self):
        return self.player_id
