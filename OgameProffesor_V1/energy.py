import data
from math import trunc






class Info:
    
    
    def __init__(self,data) -> None:
        self.fusion_plant_level = data.resource_buildings_data["Planta de fusión"]

def needed_info():
    fusion_plant_level = data.resource_buildings_data["Planta de fusión"]
    solar_plant_level = data.resource_buildings_data["Planta de energía solar"]
    satellites_count = data.resource_buildings_data["Satélite solar"]
    life_form = get_life_form(data.planet_settings)
    life_form_building = get_life_form_building(life_form)
    energy_tech_level = data.research_data["Tecnología de energía"]
    admiral_status = data.account_data["admiral"]
    engineer_status = data.account_data["engineer"]
    geologist_status = data.account_data["geologist"]
    technocrat_status = data.account_data["technocrat"]
    commander_status = data.account_data["commander"]
    command_staff_status = get_command_staff(
        admiral=admiral_status,
        engineer=engineer_status,
        geologist=geologist_status,
        technocrat=technocrat_status,
        commander=commander_status,
    )

    resultado = (
        fusion_plant_level,
        solar_plant_level,
        satellites_count,
        life_form,
        life_form_building,
        energy_tech_level,
        engineer_status,
        command_staff_status,
    )

    return resultado


def get_command_staff(admiral, engineer, geologist, technocrat, commander):
    if all([admiral, engineer, geologist, technocrat, commander]):
        return True
    else:
        return False


def get_life_form(data):
    return data["life_form"]


def get_life_form_building(life_form):
    if life_form == "rocktal":
        return data.life_forms_buildings_data["Rocktal"]["Cámara de Disrupción"]
    elif life_form == "mechas":
        return data.life_forms_buildings_data["Mechas"][
            "Transformador de alto rendimiento"
        ]
    elif life_form == "Humans":
        return "humans"
    elif life_form == "Kaelesh":
        return "kaelesh"
    else:
        return None


def energy_production(fusion_level, tech_energy_level, chamber_level):
    info = needed_info()
    fusion_energy = get_fusion_energy(
        fusion_level=fusion_level, tech_energy_level=tech_energy_level
    )
    production_bonus = get_energy_bonus(
        chamber_level=chamber_level, engineer_status=info[-2], staff_status=info[-1]
    )

    total = trunc(fusion_energy * production_bonus)
    return total


def get_energy_bonus(chamber_level: int, engineer_status: bool, staff_status: bool):
    bonus = 1

    if staff_status == True:
        bonus += 0.02

    if engineer_status == True:
        bonus += 0.1

    bonus += chamber_level * 0.015

    return bonus


def get_fusion_energy(fusion_level: int, tech_energy_level: int):
    return trunc(30 * fusion_level * (0.01 * tech_energy_level + 1.05) ** fusion_level)


def upgrade_cost(building_level: int, upgrade_factor: int, basic_cost=dict[str:int]):
    if building_level < 0:
        raise ValueError(
            f"{building_level=}, no es un argumento válido, ingrese un entero mayor a 0."
        )
    elif building_level == 0:
        return basic_cost
    else:
        metal_cost = trunc(
            (basic_cost.get("M") * upgrade_factor ** (building_level - 1))
            * building_level
        )
        crystal_cost = trunc(
            (basic_cost.get("C") * upgrade_factor ** (building_level - 1))
            * building_level
        )
        deuterium_cost = trunc(
            (basic_cost.get("D") * upgrade_factor ** (building_level - 1))
            * building_level
        )
        final_dict = {"M": metal_cost, "C": crystal_cost, "D": deuterium_cost}

        return final_dict


def energy_diff(current, next):
    return abs(current - next)





def next_step():
    current_energy = energy_production(chamber_level=get_life_form_building('rocktal'),fusion_level=)

    return current_energy


def main():
    x = Info(data=data)
    print(x)


if __name__ == "__main__":
    main()
