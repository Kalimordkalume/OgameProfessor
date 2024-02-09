class Universe:
    def __init__(self) -> None:
        self.name = "Undae"  # Undae
        self.id = "s199"  # 147
        self.flag = "es"  # ES
        self.universe_code = f"{self.name} ({self.id}-{self.flag})"
        self.fleet_debris = 0.6  # % of fleet into debris after a battle.
        self.deuterium_debris = False  # If there is deuterium on debris or not.
        self.deuterium_bonus = 0.7  # % of consumption reduced for fleets.
        self.defenders_speed = 1  # Speed for defenders.
        self.peacefull_speed = 4  # Speed for civilian units.
        self.war_speed = 1  # Speed for war units.
        self.empty_systems = True  # Empty systems are ignored if true.
        self.inactive_systems = True  # Inactive systems are ignored if true
        self.galaxy_count = 5  # Number of galaxies in the universe.
        self.planet_field_bonus = 30  # Extra planets for a planet.
        self.development_speed = 6  # Economic speed.
        self.exploration_speed = 6  # Speed for discovery misions (LF).
        self.solar_systems_count = 499  # Number of systems for each Galaxy.
        self.galaxies_circular = True  # If True the galaxies are circular.
        self.solar_systemas_circular = True  # If True the solar systemas are circular.


class UniverseTest:
    def __init__(self, universe_data: dict) -> None:
        for value, key in universe_data.items():
            setattr(self, value, key)
