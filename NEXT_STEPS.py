import data
from math import trunc


class GameData:
    def __init__(self, ogame_data_instance) -> None:
        self.ogame_data_instance = ogame_data_instance

    @property
    def get_number_of_planets_attribute(self):
        return self.ogame_data_instance.account_data.get("planets")

    @property
    def get_fusion_plant_attribute(self):
        return self.ogame_data_instance.resource_buildings_data.get("Planta de fusión")

    @property
    def get_energy_tech_attribute(self):
        return self.ogame_data_instance.research_data.get("Tecnología de energía")

    @property
    def get_life_form(self):
        life_form = self.ogame_data_instance.planet_settings.get("life_form")
        return life_form

    @property
    def get_life_form_building_attribute(self):
        life_form_type = self.get_life_form

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

    @property
    def get_solar_plant_attribute(self):
        return self.ogame_data_instance.resource_buildings_data.get(
            "Planta de energía solar"
        )

    @property
    def get_satellites_count_attribute(self):
        return self.ogame_data_instance.resource_buildings_data.get("Satélite solar")

    @property
    def get_admiral_status(self):
        return self.ogame_data_instance.account_data.get("admiral")

    @property
    def get_engineer_status(self):
        return self.ogame_data_instance.account_data.get("engineer")

    @property
    def get_geologist_status(self):
        return self.ogame_data_instance.account_data.get("geologist")

    @property
    def get_technocrat_status(self):
        return self.ogame_data_instance.account_data.get("technocrat")

    @property
    def get_commander_status(self):
        return self.ogame_data_instance.account_data.get("commander")

    @property
    def get_command_staff_status(self):
        a, b, c, d, e = (
            self.get_admiral_status,
            self.get_commander_status,
            self.get_engineer_status,
            self.get_geologist_status,
            self.get_technocrat_status,
        )

        if all((a, b, c, d, e)):
            return True
        else:
            return False


class EnergyBalance:
    def __init__(self, game_data: GameData) -> None:
        self.game_data = game_data  # Objeto de la clase Game Data que contiene toda la información de partida de la cuenta.

        self.fusion_plant_level = self.game_data.get_fusion_plant_attribute
        self.solar_plant_level = self.game_data.get_solar_plant_attribute
        self.satellites_count_level = self.game_data.get_satellites_count_attribute
        self.life_form_building_level = self.game_data.get_life_form_building_attribute
        self.energy_tech_level = self.game_data.get_energy_tech_attribute
        self.NUMBER_OF_PLANETS = self.game_data.get_number_of_planets_attribute

        self.command_staff_status = self.game_data.get_command_staff_status
        self.engineer_status = self.game_data.get_engineer_status

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

    def get_fusion_energy(self, fusion_level: int, tech_energy_level: int):
        return trunc(
            30 * fusion_level * (0.01 * tech_energy_level + 1.05) ** fusion_level
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
        BONUS_STAFF = 0.02
        BONUS_ENGINEER = 0.1
        BONUS_CHAMBER = 0.015

        bonus = 1

        if staff_status:
            bonus += BONUS_STAFF

        if engineer_status:
            bonus += BONUS_ENGINEER

        bonus += chamber_level * BONUS_CHAMBER

        return bonus

    def get_instance_data(self):
        return data.OgameDicts(data=data.ogame_data_dict)

    def conversor(self, quantity: dict[str:int]) -> float:
        return quantity["M"] + quantity["C"] * 1.5 + quantity["D"] * 3

    def next_step(self):
        # Nº de planetas con planta de fusión:
        planets = self.NUMBER_OF_PLANETS

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

        fusion_rythm = self.rythm(
            numerator=conversed_fusion_cost, denominator=diff_if_fusion
        )
        tech_rythm = self.rythm(numerator=conversed_tech_cost, denominator=diff_if_tech)
        life_form_rythm = self.rythm(
            numerator=conversed_life_cost, denominator=diff_if_LF_building
        )

        # Debugging:

        # print(f"Costes:{next_tech=}\n{next_fusion=}\n{next_building=}\n")

        # print(
        #     f"Producciones:\n{If_Fusion=}\n{If_Tech=}\n{If_Life_Building=}\n{current_production=}\n"
        # )
        # print(
        #     f"Costes convertidos:\n{conversed_fusion_cost=:_.1f}\n{conversed_tech_cost=:_.1f}\n{conversed_life_cost=:_.1f}"
        # )
        # print(
        #     f"Diferencias:\n{diff_if_fusion=:_}\n{diff_if_tech:_}\n{diff_if_LF_building:_}"
        # )

        # print(
        #     f"Tasas:\n{fusion_rythm=:_.2f}\n{tech_rythm=:_.2f}\n{life_form_rythm=:_.2f}\n"
        # )

        # El siguiente mejor step es...

        diccionario = dict(fusion=fusion_rythm, tech=tech_rythm, life=life_form_rythm)
        x = min(diccionario, key=diccionario.get)

        if x == "fusion":
            return f"Se recomienda subir el edificio de planta de fusion con una tasa de:{fusion_rythm:_.2f} del nivel actual {self.fusion_plant_level} al {self.fusion_plant_level + 1}"
        elif x == "tech":
            return f"Se recomienda subir la tecnología con una tasa de:{tech_rythm:_.2f}del nivel actual {self.energy_tech_level} al {self.energy_tech_level + 1}"
        else:
            return f"Se recomienda subir el edificio de formas de vida con una tasa de: {life_form_rythm:_.2f} del nivel actual {self.life_form_building_level} al {self.life_form_building_level + 1}"

    def rythm(self, numerator: float, denominator: float):
        """This function will take two arguments and will calculate its ratio"""
        if denominator == 0:
            return float("inf")
        else:
            return numerator / denominator

    def next_steps(
        self, desired_steps: int = None, initial_account_state: tuple[int] = None
    ):
        # Necesito que esta función llame varias veces a la función que calcula el mejor next step y luego sea capaz de alterar los datos en local para que continúe ejecutando el loop...
        # Parámetros que necesitará:
        # Necesito darle a la función el número de pasos que se desea avanzar en la secuencia...

        # Por ejemplo, 20 pasos en la secuencia.
        # Necesito pasar una tupla de 3 items que contenga el estado inicial de la estructura de la cuenta: initial_list = (planta de fusión,tecno de energía, nivel del edificio de LF.)

        # no se qué tupla inicial:

        if desired_steps == None:
            desired_steps = int(
                input(f"Indique cuántos pasos de la secuencia desea calcular: ")
            )

        if initial_account_state != None:
            FUSION, ENERGY, LF_BUILDING, PLANETS = initial_account_state
            fusion_level = FUSION
            energy_level = ENERGY
            lf_level = LF_BUILDING
            planets = PLANETS
        else:
            fusion_level = int(input(f"Indique el nivel de su fusión actual: "))
            energy_level = int(
                input(f"Indique el nivel de su tecnología de energía actual: ")
            )
            lf_level = int(
                input(f"Indique el nivel del edificio de formas de vida actual: ")
            )
            planets = int(
                input(
                    f"Indique el número de planetas en los que desea usar plantas de fusión:"
                )
            )

        engineer_status = self.engineer_status
        command_staff_status = self.command_staff_status

        resultados = {}

        for step in range(1, desired_steps + 1):
            production_if_fusion = self.get_energy_production(
                bonus=self.get_energy_bonus(
                    chamber_level=lf_level,
                    engineer_status=engineer_status,
                    staff_status=command_staff_status,
                ),
                energy_sources=self.get_fusion_energy(
                    fusion_level=fusion_level + 1,
                    tech_energy_level=energy_level,
                ),
            )
            production_if_tech = self.get_energy_production(
                bonus=self.get_energy_bonus(
                    chamber_level=lf_level,
                    engineer_status=engineer_status,
                    staff_status=command_staff_status,
                ),
                energy_sources=self.get_fusion_energy(
                    fusion_level=fusion_level, tech_energy_level=energy_level + 1
                ),
            )
            production_if_life = self.get_energy_production(
                bonus=self.get_energy_bonus(
                    chamber_level=lf_level + 1,
                    engineer_status=engineer_status,
                    staff_status=command_staff_status,
                ),
                energy_sources=self.get_fusion_energy(
                    fusion_level=fusion_level, tech_energy_level=energy_level
                ),
            )
            current_production = self.get_energy_production(
                bonus=self.get_energy_bonus(
                    chamber_level=lf_level,
                    engineer_status=engineer_status,
                    staff_status=command_staff_status,
                ),
                energy_sources=self.get_fusion_energy(
                    fusion_level=fusion_level, tech_energy_level=energy_level
                ),
            )

            production_difference_if_fusion = abs(
                current_production - production_if_fusion
            )
            production_difference_if_energy_tech = abs(
                current_production - production_if_tech
            )
            production_difference_if_life_form = abs(
                current_production - production_if_life
            )

            next_converted_cost_for_fusion = self.conversor(
                quantity=self.get_fusion_plant_cost(plant_level=fusion_level)
            )
            next_converted_cost_for_energy = self.conversor(
                quantity=self.get_energy_tech_cost(energy_level=energy_level)
            )
            next_converted_cost_for_life_form = self.conversor(
                quantity=self.get_life_form_building_cost(
                    life_form_building_level=lf_level
                )
            )

            fusion_rythm = self.rythm(
                denominator=production_difference_if_fusion,
                numerator=next_converted_cost_for_fusion * planets,
            )
            energy_tech_rythm = self.rythm(
                denominator=production_difference_if_energy_tech,
                numerator=next_converted_cost_for_energy,
            )
            life_form_rythm = self.rythm(
                denominator=production_difference_if_life_form,
                numerator=next_converted_cost_for_life_form * planets,
            )

            # A esta altura el bucle debe saber cuál es la mejor tasa y arrojarla.

            # Updateamos los valores:
            resultados.update({"fusion": fusion_rythm})
            resultados.update({"energy_tech": energy_tech_rythm})
            resultados.update({"life_form": life_form_rythm})

            # Escogemos el mínimo:

            resultado = min(resultados, key=resultados.get)

            if resultado == "energy_tech":
                msg = f"Step {step}:\nTecno de energía al {energy_level+1}.\n"
                energy_level += 1
                print(msg)
                continue
            elif resultado == "fusion":
                msg = f"Step {step}:\nPlanta de fusión (todos los planetas) al {fusion_level+1}.\n"
                fusion_level += 1
                print(msg)
                continue
            else:
                msg = f"Step {step}:\nEdificio de LifeForms (todos los planetas) al {lf_level+1}.\n"
                lf_level += 1
                print(msg)
                continue


def main():
    ogame_data_instance = data.OgameData(data=data.ogame_data_dict)
    game_data = GameData(ogame_data_instance)
    instance = EnergyBalance(game_data)
    instance.next_steps()


if __name__ == "__main__":
    main()
