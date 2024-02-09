import tools


class DisruptionChamber:
    _BASIC_COSTS = {"M": 20_000, "C": 15_000, "D": 10_000}
    _ENERGY_BONUS = 1.5 / 100
    _CONSUMPTION_BONUS = -0.5 / 100
    _UPGRADE_FACTOR = 1.2

    def __init__(self, LEVEL) -> None:
        self.level = LEVEL
        self.__upgrade_costs = tools.upgrade_cost(
            lvl=self.level,
            upgrade_factor=self.upgrade_factor,
            basic_cost=self.basic_costs,
        )

    @property
    def basic_costs(self):
        return self._BASIC_COSTS

    @property
    def energy_bonus(self):
        return self._ENERGY_BONUS

    @property
    def consumption_bonus(self):
        return self._CONSUMPTION_BONUS

    @property
    def upgrade_factor(self):
        return self._UPGRADE_FACTOR

    @property
    def upgrade_costs(self):
        return self.__upgrade_costs
