from classes.disruptionchamber import DisruptionChamber
from classes.energytech import EnergyTech
from classes.fusionplant import FusionPlant
from classes.accounts import Account, AccountTest
from classes.universes import UniverseTest
from math import trunc
from classes.planets import PlanetTest
import data


def fusion_production(lvl: int, energy_level: int):
    return trunc(30 * lvl * (0.01 * energy_level + 1.05) ** lvl)


def check_engineer_status(account_instance: Account()):
    if account_instance.engineer_check == True:
        return 0.1
    else:
        return 0


def check_command_staff_status(account_instance: Account()):
    if account_instance.commander_group_check == True:
        return 0.02
    else:
        return 0


def total_energy_production():
    chamber_level = 10
    fusion_level = 20
    energy_level = 16

    chamber_instance = DisruptionChamber(chamber_level)
    fusion_instance = FusionPlant(fusion_level)
    energy_instance = EnergyTech(energy_level)
    account_instance = Account()

    fusion_energy = fusion_production(fusion_instance.level, energy_instance.level)
    bonus = (
        1
        + (chamber_instance.level * chamber_instance.energy_bonus)
        + check_command_staff_status(account_instance=account_instance)
        + check_engineer_status(account_instance=account_instance)
    )
    total_energy = trunc(fusion_energy * bonus)

    return total_energy


def run():
    planet_info = get_planet_info()
    account_info = get_account_info()
    universe_info = get_universe_info()
    print(
        f"{planet_info.__dict__=}\n{account_info.__dict__=}\n{universe_info.__dict__=}"
    )


if __name__ == "__main__":
    run()
