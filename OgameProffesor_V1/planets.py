class PlanetTest:
    def __init__(self, planet_data: dict) -> None:
        for key, value in planet_data.items():
            setattr(self, key, value)
