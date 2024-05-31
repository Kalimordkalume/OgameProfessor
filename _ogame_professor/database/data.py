def conversion(resources_list: list) -> float:
    metal = resources_list[0]
    crystal = resources_list[1]
    deuterium = resources_list[2]

    total_umes_cost = metal + crystal * 1.5 + deuterium * 3

    return total_umes_cost


ENTITIES_ID = {
    0: "Metal Mine",
    1: "Crystal Mine",
    2: "Deuterium Synthetizer",
    3: "Solar Plant",
    4: "Robotics Factory",
    5: "Astrophysics",
}
METAL_BASIC_COSTS = {
    "Metal Mine": 60,
    "Crystal Mine": 48,
    "Deuterium Synthetizer": 225,
    "Solar Plant": 10,
    "Robotics Factory": 400,
    "Astrophysics": 20,
}

CRYSTAL_BASIC_COSTS = {
    "Metal Mine": 15,
    "Crystal Mine": 24,
    "Deuterium Synthetizer": 75,
    "Solar Plant": 10,
    "Robotics Factory": 120,
    "Astrophysics": 20,
}
DEUTERIUM_BASIC_COSTS = {
    "Metal Mine": 0,
    "Crystal Mine": 0,
    "Deuterium Synthetizer": 200,
    "Solar Plant": 10,
    "Robotics Factory": 20,
    "Astrophysics": 20,
}


TOTAL_BASIC_COSTS = {
    "Metal Mine": [
        METAL_BASIC_COSTS.get("Metal Mine"),
        CRYSTAL_BASIC_COSTS.get("Metal Mine"),
        DEUTERIUM_BASIC_COSTS.get("Metal Mine"),
    ],
    "Crystal Mine": [
        METAL_BASIC_COSTS.get("Crystal Mine"),
        CRYSTAL_BASIC_COSTS.get("Crystal Mine"),
        DEUTERIUM_BASIC_COSTS.get("Crystal Mine"),
    ],
    "Deuterium Synthetizer": [
        METAL_BASIC_COSTS.get("Deuterium Synthetizer"),
        CRYSTAL_BASIC_COSTS.get("Deuterium Synthetizer"),
        DEUTERIUM_BASIC_COSTS.get("Deuterium Synthetizer"),
    ],
    "Solar Plant": [
        METAL_BASIC_COSTS.get("Solar Plant"),
        CRYSTAL_BASIC_COSTS.get("Solar Plant"),
        DEUTERIUM_BASIC_COSTS.get("Solar Plant"),
    ],
    "Robotics Factory": [
        METAL_BASIC_COSTS.get("Robotics Factory"),
        CRYSTAL_BASIC_COSTS.get("Robotics Factory"),
        DEUTERIUM_BASIC_COSTS.get("Robotics Factory"),
    ],
    "Astrophysics": [
        METAL_BASIC_COSTS.get("Astrophysics"),
        CRYSTAL_BASIC_COSTS.get("Astrophysics"),
        DEUTERIUM_BASIC_COSTS.get("Astrophysics"),
    ],
}
TOTAL_BASIC_COSTS_IN_UMES = {
    "Metal Mine": conversion(resources_list=TOTAL_BASIC_COSTS.get("Metal Mine")),
    "Crystal Mine": conversion(resources_list=TOTAL_BASIC_COSTS.get("Crystal Mine")),
    "Deuterium Synthetizer": conversion(
        resources_list=TOTAL_BASIC_COSTS.get("Deuterium Synthetizer")
    ),
    "Solar Plant": conversion(resources_list=TOTAL_BASIC_COSTS.get("Solar Plant")),
    "Robotics Factory": conversion(
        resources_list=TOTAL_BASIC_COSTS.get("Robotics Factory")
    ),
    "Astrophysics": conversion(resources_list=TOTAL_BASIC_COSTS.get("Astrophysics")),
}

BASIC_PRODUCTION_RATES = {
    "Metal Mine": 30,
    "Crystal Mine": 20,
    "Deuterium Synthetizer": 10,
    "Solar Plant": 10,
    "Robotics Factory": 20,
    "Astrophysics": 20,
}

USER_MINES = {
    "Metal Mine": 10,
    "Crystal Mine": 7,
    "Deuterium Synthetizer": 5,
}
USER_FACILITIES = {
    "Robotics Factory": 5,
    "Nanite Factory": 5,
}

USER_ACCOUNT = {
    "Andromeda": {
        "Metal Mine": 30,
        "Crystal Mine": 22,
        "Deuterium Synthetizer": 23,
        "Robotics Factory": 10,
        "Nanite Factory": 10,
    },
    "Geminis": {
        "Metal Mine": 15,
        "Crystal Mine": 6,
        "Deuterium Synthetizer": 21,
        "Robotics Factory": 10,
        "Nanite Factory": 0,
    },
    "Borealis": {
        "Metal Mine": 11,
        "Crystal Mine": 16,
        "Deuterium Synthetizer": 20,
        "Robotics Factory": 10,
        "Nanite Factory": 0,
    },
    "Cygnus": {
        "Metal Mine": 10,
        "Crystal Mine": 9,
        "Deuterium Synthetizer": 5,
        "Robotics Factory": 10,
        "Nanite Factory": 0,
    },
    "Arcturus": {
        "Metal Mine": 7,
        "Crystal Mine": 5,
        "Deuterium Synthetizer": 5,
        "Robotics Factory": 10,
        "Nanite Factory": 0,
    },
    "Orion": {
        "Metal Mine": 20,
        "Crystal Mine": 15,
        "Deuterium Synthetizer": 2,
        "Robotics Factory": 10,
        "Nanite Factory": 0,
    },
}


UNIVERSE_DATA = {
    "NAME": "Random",
    "ECONOMY_SPEED": 5,
    "RESEARCH_SPEED": 10,
    "IS_CIRCULAR": True,
}

ACCOUNT_TECHNOLOGIES = {}

ACCOUNT_DATA = {
    "PLANET_ENTITIES": USER_ACCOUNT,
    "TECHNOLOGIES": ACCOUNT_TECHNOLOGIES,
    "COMMANDER": True,
    "ENGINEER": True,
    "TECHNOCRAT": True,
    "ADMIRAL": True,
    "GEOLOGIST": True,
    "CLASS": "DISCOVERER",
    "DARK_MATTER_COUNT": 0,
}
