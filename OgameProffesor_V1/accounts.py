from enum import Enum
from classes.universes import UniverseTest
from classes.planets import PlanetTest

import data


class AccountTest:
    def __init__(self, account_data=dict) -> None:
        for key, value in account_data.items():
            setattr(self, key, value)

        self.universe_info = UniverseTest(universe_data=data.universe_data)
