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
            print(f"---------------------------------------------------------")
            print(f"{game.away_team.team_name} @ {game.home_team.team_name}")
            print(f"{game.park} - {game.game_time}")
            print(f"---------------------------------------------------------")
            print(f"{game.away_team.team_tricode} - {game.away_team.team_name}")
            if game.away_team.batters:
                for batter in game.away_team.batters:
                    print(
                        f"{batter.batting_num}, {batter.player_name}, {batter.player_id}, {batter.player_handedness}, {batter.player_position}"
                    )
            print(f"{game.home_team.team_tricode} - {game.home_team.team_name}")
            if game.home_team.batters:
                for batter in game.home_team.batters:
                    print(
                        f"{batter.batting_num}, {batter.player_name}, {batter.player_id}, {batter.player_handedness}, {batter.player_position}"
                    )
