from math import trunc
from typing import Tuple


class Universe:
    def __init__(
        self, name: str = "Undae", economy_speed: int = 6, galaxy_count: int = 5
    ) -> None:
        self.name = name
        self.economy_speed = economy_speed
        self.galaxy_count = galaxy_count


class Planet:
    def __init__(self, coordinates) -> None:
        self.universe = Universe()

        self.solar_system = None
        self.position = None
        self.coordinates = coordinates
        self.resource_building_list = None
        self.basic_metal_production = 30
        self.basic_crystal_production = 15

        self.metal_count = None
        self.crystal_count = None
        self.deuterium_count = None
        self.energy_count = None
        self.food_count = None

        self._coordinates = (
            None  # Atributo privado para poder almacenar las coordenadas.
        )

    @property
    def coordinates(self):
        """_summary_
            Función que sirve para generar el atributo coordinates. Para ello se utiliza el decorador @property, que permite llamar a un método de una clase como si fuera un atributo.
        Returns:
            _type_: Retorna un atributo privado inicializado en None para poder modificar las coordenadas en el futuro tras las correspondientes verificaciones.
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        """Junto con el decorador @property, esta función modificará el valor del atributo coordinates.

        Args:
            new_coordinates (tuple): Nombre simbólico para diferenciar las coordenadas de inicio de las finales tras las validaciones.

        Raises:
            ValueError: _description_
        """
        if self.validate_coordinates(new_coordinates):
            self._coordinates = new_coordinates
            self.generate_location()
        else:
            raise ValueError("Unvalid coordinates, make sure to check the values.")

    def validate_coordinates(self, new_coordinates):
        """Función que se ocupará de comprobar que las coordenadas que ha metido el usuario o se hayan cargado de alguna fuente son correctas.

        Args:
            new_coordinates (tuple): Nombre simbólico, aquí se meterían las coordenadas iniciales.

        Returns:
            _type_: _description_
        """
        cond1 = new_coordinates[0] <= self.universe.galaxy_count
        cond2 = 1 <= new_coordinates[1] <= 499
        cond3 = 1 <= new_coordinates[2] <= 15

        if all((cond1, cond2, cond3)) == True:
            return True
        else:
            return False

    def generate_location(self):
        """Función que modificará los parámetros iniciales garantizando que son correctos."""
        # Generar galaxia, sistema solar y posición según las coordenadas

        self.galaxy = self.coordinates[0]
        self.solar_system = self.coordinates[1]
        self.position = self.coordinates[2]


class ResourceBuilding:
    """Clase principal que amalgama a los edificios de la categoría recursos de OGame."""

    def __init__(self) -> None:
        """Inicializador de un edificio de recursos.

        Args:
            name (str): Nombre del edificio de recursos o mina.
            level (int): Nivel del edificio
            basic_production (int): Producción base del edificio.
        """
        None
        self.level = None
        self.productive_base = None
        self.consumption_base = None
        self.production_factor = None
        self.time_cost = None
        self.next_level = None


class MetalMine(ResourceBuilding):

    def __init__(self, level: int) -> None:
        # Inicializador de la subclase MetalMine.
        # Genera un objeto de la clase Metal Mine heredando atributos y métodos de la clase superior.

        self.level = level
        self.productive_parameter = 30
        self.production_factor = 1.1
        self.consumption_base = 10
        self.time_cost = None  # Hay que implementar la función.
        self.next_level = None  # Hay que implementar la función.


class CrystalMine(ResourceBuilding):

    def __init__(self, level: int) -> None:

        self.level = level
        self.productive_parameter = 20
        self.production_factor = 1.1
        self.consumption_base = 10
        self.time_cost = None  # Hay que implementar la función.
        self.next_level = None  # Hay que implementar la función.


class DeuteriumSynthetiser(ResourceBuilding):

    def __init__(self, level: int) -> None:

        self.level = level
        self.productive_parameter = 10
        self.production_factor = 1.1
        self.consumption_base = 20
        self.time_cost = None  # Hay que implementar la función.
        self.next_level = None  # Hay que implementar la función.


class SolarPlant(ResourceBuilding):
    def __init__(self, level: int) -> None:

        self.level = level
        self.productive_parameter = 30
        self.production_factor = 1.1
        self.consumption_base = 10
        self.time_cost = None  # Hay que implementar la función.
        self.next_level = None  # Hay que implementar la función.


class FusionPlant(ResourceBuilding):
    def __init__(self, level: int) -> None:

        self.level = level
        self.productive_parameter = 30
        self.production_factor = 1.1
        self.consumption_base = 10
        self.time_cost = None  # Hay que implementar la función.
        self.next_level = None  # Hay que implementar la función.


class MetalStorage(ResourceBuilding):

    def __init__(self, level: int) -> None:
        self.level = level
        self.upgrade_facotr = 2


class CrystalStorage(ResourceBuilding):

    def __init__(self, level: int) -> None:
        self.level = level
        self.upgrade_facotr = 2


class DeuteriumStorage(ResourceBuilding):

    def __init__(self, level: int) -> None:
        self.level = level
        self.upgrade_facotr = 2


class SolarSatellite(ResourceBuilding):

    def __init__(self, count: int) -> None:

        self.count = count


def main():
    val = (3, 467, 14)
    black_hole = Planet(coordinates=val)

    # Los planetas tienen edificios:

    # Hay que sacar el esquema de datos desde el archivo DATA


if __name__ == "__main__":
    main()
