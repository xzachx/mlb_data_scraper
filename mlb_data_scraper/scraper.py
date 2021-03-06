import argparse
from mlb_data_scraper.page import Page


class Scraper(object):
    """Main Web Scraper class"""

    def __init__(self):
        self.args = None
        self.parse_args()

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
            "--date",
            required=False,
            help='Game date if not today (YYYY-MM-DD format)',
        )
        self.args = parser.parse_args()

    def run(self):
        if self.args.date:
            print(f"Running scraper for {self.args.date}")
        else:
            print("No date specified, running scraper for today's lineups")
