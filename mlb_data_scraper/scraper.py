import argparse
import datetime
from mlb_data_scraper.page import Page


class Scraper(object):
    """Main Web Scraper class"""

    def __init__(self):
        self.args = None
        self.parse_args()
        self.page = None

    def parse_args(self):
        """
        Parses arguments from the command line

        Returns
        -------
        None
        """

        parser = argparse.ArgumentParser()
        # parser.add_argument(
        #     "--version", action="version", version="%(prog)s {version}".format(version=__version__)
        # )
        parser.add_argument(
            "--date", required=False, help="Game date if not today (YYYY-MM-DD format)",
        )
        self.args = parser.parse_args()

    def run(self):
        self.page = Page(date=self.args.date)
        self.page.get_page()

        for game in self.page.get_games():
            print(f"{game.away_team.team_name} ({game.away_team.team_tricode}) AT {game.home_team.team_name} ({game.home_team.team_tricode})")
