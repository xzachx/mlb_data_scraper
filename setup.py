#!/usr/bin/env python
"""Archerfish: testing suite for data quality issues in sales and returns data"""

__maintainer__ = "Zach Brown"
__credits__ = ["Zach Brown"]
__docformat__ = "restructuredtext"
__email__ = ""

from setuptools import setup, find_packages

# Basics ----------------------------------------------------------------------

NAME = "mlb_data_scraper"
VERSION = {}
with open("mlb_data_scraper/_version.py") as fp:
    exec(fp.read(), VERSION)
DESCRIPTION = "Downloads starting lineups from mlb.com"
LONG_DESCRIPTION = DESCRIPTION

# Dependencies ----------------------------------------------------------------

SETUP_DEPS = ()
INSTALL_DEPS = (
    "beautifulsoup4",
    "pandas",
    "requests",
)
EXTRAS_DEPS = {}
TESTS_DEPS = ()
DEPS_SEARCH_URIS = ()

# Entry Point -----------------------------------------------------------------

ENTRY_POINTS = {"console_scripts": ["mlb_data_scraper = mlb_data_scraper.mlb_data_scraper:run_mlb_data_scraper"]}

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION["__version__"],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=", ".join(__credits__),
        maintainer=__maintainer__,
        maintainer_email=__email__,
        setup_requires=SETUP_DEPS,
        install_requires=INSTALL_DEPS,
        extras_require=EXTRAS_DEPS,
        tests_require=TESTS_DEPS,
        packages=find_packages(exclude=["test", "test.*"]),
        include_package_data=True,
        entry_points=ENTRY_POINTS,
        scripts=[],
    )
