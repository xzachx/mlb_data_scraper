import datetime
import requests
from bs4 import BeautifulSoup
from mlb_data_scraper.game import Game


class Page:
    """Class containing data for full page"""

    def __init__(self, date=None, url=None):
        self.date = date
        self.url = url
        self.page = None
        self.content = None
        self.games = []

    def set_url(self):
        base_url = "https://www.mlb.com/starting-lineups/"
        if self.url is not None:
            return
        elif self.date is not None:
            try:
                datetime.datetime.strptime(self.date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")

            self.url = base_url + self.date
        else:
            self.url = base_url + datetime.date.strftime(datetime.date.today(), "%Y-%m-%d")
        print(f"Running scraper for {self.url}")

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

    def get_games(self):
        return self.games

    def get_page(self):
        self.set_url()
        self.download_page()
        self.set_page_content()
        self.set_games()
