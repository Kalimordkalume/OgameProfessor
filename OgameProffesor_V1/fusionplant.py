import tools


class FusionPlant:
    __BASIC_COSTS = {"M": 900, "C": 360, "D": 180}
    __UPGRADE_FACTOR = 1.8

    def __init__(self, LEVEL: int) -> None:
        self.level = LEVEL
        self.__upgrade_costs = tools.upgrade_cost(
            lvl=self.level,
            upgrade_factor=self.__UPGRADE_FACTOR,
            basic_cost=self.__BASIC_COSTS,
        )
        self.consumption = tools.fusion_consumption(self.level)

    @property
    def basic_costs(self):
        return self.__BASIC_COSTS

    @property
    def upgrade_factor(self):
        return self.__UPGRADE_FACTOR

    @property
    def upgrade_costs(self):
        return self.__upgrade_costs
