from math import trunc


def upgrade_cost(
    lvl: int, upgrade_factor: int, basic_cost=dict[str:int]
) -> (dict[str:int], float):
    if lvl < 0:
        raise ValueError(
            f"{lvl=}, no es un argumento válido, ingrese un entero mayor a 0."
        )
    elif lvl == 0:
        return basic_cost
    else:
        metal_cost = trunc((basic_cost.get("M") * upgrade_factor ** (lvl - 1)) * lvl)
        crystal_cost = trunc((basic_cost.get("C") * upgrade_factor ** (lvl - 1)) * lvl)
        deuterium_cost = trunc(
            (basic_cost.get("D") * upgrade_factor ** (lvl - 1)) * lvl
        )
        final_dict = {"M": metal_cost, "C": crystal_cost, "D": deuterium_cost}

        return (final_dict, conversor(final_dict))


def conversor(quantity: dict[str:int]) -> float:
    return quantity["M"] + quantity["C"] * 1.5 + quantity["D"] * 3


def fusion_production(lvl: int, energy_level: int):
    return trunc(30 * lvl * (0.01 * energy_level + 1.05) ** lvl)


def fusion_consumption(lvl: int):
    return trunc(10 * lvl * 1.1**lvl)
