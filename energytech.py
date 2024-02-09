import tools


class EnergyTech:
    __BASIC_COSTS = {"M": 0, "C": 800, "D": 400}
    __UPGRADE_FACTOR = 2

    def __init__(self, LEVEL: int) -> None:
        self.level = LEVEL
        self.__upgrade_costs = tools.upgrade_cost(
            lvl=self.level,
            upgrade_factor=self.__UPGRADE_FACTOR,
            basic_cost=self.__BASIC_COSTS,
        )

    @property
    def basic_costs(self):
        return self.__BASIC_COSTS

    def upgrade_factor(self):
        return self.__UPGRADE_FACTOR

    def upgrade_costs(self):
        return self.__upgrade_costs
