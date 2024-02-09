import data
from math import trunc


class EnergyBalance:
    def __init__(self) -> None:
        self.ogame_data_instance = (
            self.get_instance_data()
        )  # Objeto de la clase Ogame Data que contiene toda la información de partida de la cuenta.

        self.fusion_plant_level = self.get_fusion_plant_attribute()
        self.solar_plant_level = self.get_solar_plant_attribute()
        self.satellites_count_level = self.get_satellites_count()
        self.life_form_building_level = self.get_life_form_building()
        self.energy_tech_level = self.get_energy_tech_attribute()

        self.command_staff_status = self.get_command_staff_status()
        self.engineer_status = self.get_engineer_status()

        # Computed values:
        self.energy_from_fusion = self.get_fusion_energy(
            self.fusion_plant_level, self.energy_tech_level
        )

        self.total_bonus = self.get_energy_bonus(
            self.life_form_building_level,
            self.engineer_status,
            self.command_staff_status,
        )

        self.total_energy_production = self.get_energy_production(
            self.total_bonus, self.energy_from_fusion
        )

        self.life_form_building_cost = self.get_life_form_building_cost(
            life_form_building_level=self.life_form_building_level
        )

        self.fusion_cost = self.get_fusion_plant_cost(
            plant_level=self.fusion_plant_level
        )
        self.energy_tech_cost = self.get_energy_tech_cost(
            energy_level=self.energy_tech_level
        )

    def get_fusion_plant_cost(self, plant_level: int):
        basic_cost = {"M": 900, "C": 360, "D": 180}
        upgrade_factor = 1.8

        if plant_level < 0:
            raise ValueError(
                f"{plant_level=},no es un argumento válido, ingrese un número mayor a 0."
            )
        elif plant_level == 0:
            return basic_cost
        else:
            metal_cost = trunc((basic_cost.get("M") * upgrade_factor ** (plant_level)))
            crystal_cost = trunc(
                (basic_cost.get("C") * upgrade_factor ** (plant_level))
            )
            deuterium_cost = trunc(
                (basic_cost.get("D") * upgrade_factor ** (plant_level))
            )
            final_dict = {"M": metal_cost, "C": crystal_cost, "D": deuterium_cost}

            return final_dict

    def get_energy_tech_cost(self, energy_level: int):
        basic_cost = {"M": 0, "C": 800, "D": 400}
        upgrade_factor = 2

        if energy_level < 0:
            raise ValueError(
                f"{energy_level=},no es un argumento válido, ingrese un número mayor a 0."
            )
        elif energy_level == 0:
            return basic_cost
        else:
            metal_cost = trunc(
                (basic_cost.get("M") * (upgrade_factor ** (energy_level)))
            )
            crystal_cost = trunc(
                (basic_cost.get("C") * (upgrade_factor ** (energy_level)))
            )
            deuterium_cost = trunc(
                (basic_cost.get("D") * (upgrade_factor ** (energy_level)))
            )
            final_dict = {"M": metal_cost, "C": crystal_cost, "D": deuterium_cost}

            return final_dict

    def get_life_form_building_cost(self, life_form_building_level: int):
        basic_cost = {"M": 20_000, "C": 15_000, "D": 10_000}
        upgrade_factor = 1.2
        if life_form_building_level < 0:
            raise ValueError(
                f"{life_form_building_level=}, no es un argumento válido, ingrese un entero mayor a 0."
            )

        elif life_form_building_level == 0:
            return basic_cost
        else:
            metal_cost = trunc(
                (basic_cost.get("M") * upgrade_factor ** (life_form_building_level - 1))
                * life_form_building_level
            )

            crystal_cost = trunc(
                (basic_cost.get("C") * upgrade_factor ** (life_form_building_level - 1))
                * life_form_building_level
            )
            deuterium_cost = trunc(
                (basic_cost.get("D") * upgrade_factor ** (life_form_building_level - 1))
                * life_form_building_level
            )
            final_dict = {"M": metal_cost, "C": crystal_cost, "D": deuterium_cost}

            return final_dict

    def get_energy_production(self, bonus, energy_sources):
        total = trunc(bonus * energy_sources)

        return total

    def get_energy_bonus(
        self, chamber_level: int, engineer_status: bool, staff_status: bool
    ):
        bonus = 1

        if staff_status == True:
            bonus += 0.02

        if engineer_status == True:
            bonus += 0.1

        bonus += chamber_level * 0.015

        return bonus

    def get_fusion_energy(self, fusion_level: int, tech_energy_level: int):
        return trunc(
            30 * fusion_level * (0.01 * tech_energy_level + 1.05) ** fusion_level
        )

    def get_instance_data(self):
        return data.OgameData(data=data.ogame_data_dict)

    def get_fusion_plant_attribute(self):
        return self.ogame_data_instance.resource_buildings_data.get("Planta de fusión")

    def get_solar_plant_attribute(self):
        return self.ogame_data_instance.resource_buildings_data.get(
            "Planta de energía solar"
        )

    def get_satellites_count(self):
        return self.ogame_data_instance.resource_buildings_data.get("Satélite solar")

    def get_life_form(self):
        life_form = self.ogame_data_instance.planet_settings.get("life_form")
        return life_form

    def get_life_form_building(self):
        life_form_type = self.get_life_form()

        building_dict = self.ogame_data_instance.life_forms_buildings_data.get(
            life_form_type
        )

        match life_form_type:
            case "rocktal":
                return self.ogame_data_instance.life_forms_buildings_data[
                    "rocktal"
                ].get("Cámara de Disrupción")
            case "mechas":
                return building_dict["Transformador de alto rendimiento"]
            case _:
                raise ValueError(f"{life_form_type=} No es un valor válido.")

    def get_energy_tech_attribute(self):
        return self.ogame_data_instance.research_data.get("Tecnología de energía")

    def conversor(self, quantity: dict[str:int]) -> float:
        return quantity["M"] + quantity["C"] * 1.5 + quantity["D"] * 3

    def next_step(self):
        # Nº de planetas con planta de fusión:
        planets = 8

        # Costes:
        next_tech = self.energy_tech_cost
        next_fusion = self.fusion_cost
        next_building = self.life_form_building_cost

        # Producciones:
        # Actual:
        current_production = self.total_energy_production

        # Next Production:

        If_Fusion = self.get_energy_production(
            bonus=self.total_bonus,
            energy_sources=self.get_fusion_energy(
                fusion_level=self.fusion_plant_level + 1,
                tech_energy_level=self.energy_tech_level,
            ),
        )
        If_Tech = self.get_energy_production(
            bonus=self.total_bonus,
            energy_sources=self.get_fusion_energy(
                fusion_level=self.fusion_plant_level,
                tech_energy_level=self.energy_tech_level + 1,
            ),
        )

        If_Life_Building = self.get_energy_production(
            bonus=self.get_energy_bonus(
                chamber_level=self.life_form_building_level + 1,
                engineer_status=self.engineer_status,
                staff_status=self.engineer_status,
            ),
            energy_sources=self.get_fusion_energy(
                fusion_level=self.fusion_plant_level,
                tech_energy_level=self.energy_tech_level,
            ),
        )
        conversed_fusion_cost = self.conversor(next_fusion) * planets  # checked
        conversed_tech_cost = self.conversor(next_tech)  # checked
        conversed_life_cost = self.conversor(next_building) * planets  # checked

        # Diferencias de producciones:

        diff_if_fusion = abs(If_Fusion - current_production)
        diff_if_tech = abs(If_Tech - current_production)
        diff_if_LF_building = abs(If_Life_Building - current_production)

        # Tasas:

        fusion_derivate = conversed_fusion_cost / diff_if_fusion
        tech_derivate = conversed_tech_cost / diff_if_tech
        life_form_derivate = conversed_life_cost / diff_if_LF_building

        # Debugging:

        print(f"Costes:{next_tech=}\n{next_fusion=}\n{next_building=}\n")

        print(
            f"Producciones:\n{If_Fusion=}\n{If_Tech=}\n{If_Life_Building=}\n{current_production=}\n"
        )
        print(
            f"Costes convertidos:\n{conversed_fusion_cost=:_.1f}\n{conversed_tech_cost=:_.1f}\n{conversed_life_cost=:_.1f}"
        )
        print(
            f"Diferencias:\n{diff_if_fusion=:_}\n{diff_if_tech:_}\n{diff_if_LF_building:_}"
        )

        print(
            f"Tasas:\n{fusion_derivate=:_.2f}\n{tech_derivate=:_.2f}\n{life_form_derivate=:_.2f}\n"
        )

        # El siguiente mejor step es...

        diccionario = dict(
            fusion=fusion_derivate, tech=tech_derivate, life=life_form_derivate
        )
        x = min(diccionario, key=diccionario.get)

        if x == "fusion":
            return f"Se recomienda subir el edificio de planta de fusion con una tasa de:{fusion_derivate:_.2f} del nivel actual {self.fusion_plant_level} al {self.fusion_plant_level + 1}"
        elif x == "tech":
            return f"Se recomienda subir la tecnología con una tasa de:{tech_derivate:_.2f}del nivel actual {self.energy_tech_level} al {self.energy_tech_level + 1}"
        else:
            return f"Se recomienda subir el edificio de formas de vida con una tasa de: {life_form_derivate:_.2f} del nivel actual {self.life_form_building_level} al {self.life_form_building_level + 1}"


def main():
    instance = EnergyBalance()
    print(instance.next_step())


if __name__ == "__main__":
    main()
