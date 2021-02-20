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


def get_attribute(tag, attribute):
    """Returns specified attribute value from within an HTML tag"""
    attr = tag[attribute]
    return attr


class Game:
    """Class containing data for an individual game"""

    def __init__(self, data):
        self.data = data
        self.home_team_tricode = None
        self.away_team_tricode = None

    def get_teams(self):
        """Extract team level data"""
        self.home_team_tricode = get_attribute(
            self.data.select(".starting-lineups__team-names .starting-lineups__team-name--home")[
                0
            ].a,
            "data-tri-code",
        )
        self.away_team_tricode = get_attribute(
            self.data.select(".starting-lineups__team-names .starting-lineups__team-name--away")[
                0
            ].a,
            "data-tri-code",
        )
