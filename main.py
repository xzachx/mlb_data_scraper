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
        self.home_team_tricode = None
        self.home_team_name = None
        self.away_team_tricode = None
        self.away_team_name = None

    def set_team_blocks(self):
        """Extract code blocks for home and away teams"""
        teams = self.data.select(".starting-lineups__team-names")[0]
        self.home_team = teams.select(".starting-lineups__team-name--home")[0]
        self.away_team = teams.select(".starting-lineups__team-name--away")[0]

    def set_team_tricodes(self):
        """Set team tri-codes"""
        self.home_team_tricode = self.home_team.a["data-tri-code"]
        self.away_team_tricode = self.away_team.a["data-tri-code"]

    def set_team_names(self):
        """Set team names"""
        self.home_team_name = self.home_team.a.get_text().strip()
        self.away_team_name = self.away_team.a.get_text().strip()
