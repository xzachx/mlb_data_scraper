import requests
from bs4 import BeautifulSoup
from game import Game


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

    def set_games(self):
        """Return a list of games and all of their data"""
        self.games = [
            Game(game) for game in self.content.find_all(class_="starting-lineups__matchup")
        ]
