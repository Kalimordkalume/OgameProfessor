from django import forms


class AccountCharacteristicsForm(forms.Form):
    planet_count = forms.IntegerField(
        label="Number of Planets: ",
        min_value=1,
        max_value=500,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-slate-600",
                "placeholder": "1, 2, 3, ...",
            }
        ),
        required=True,
    )
    player_class = forms.ChoiceField(
        choices=[
            ("none", "None"),
            ("human", "Humans"),
            ("rock_tal", "Rock'tal"),
            ("kaelesh", "Kaelesh"),
            ("mechas", "Mechas"),
        ],
        label="Player Class: ",
        widget=forms.Select(
            attrs={
                "class": "bg-slate-600",
            }
        ),
        required=True,
    )
    universe_economy = forms.IntegerField(
        label="Economy Speed: ",
        min_value=1,
        max_value=500,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                "class": "bg-slate-600",
            }
        ),
        required=True,
    )


class PlanetCharacteristicsForm(forms.Form):
    # Planet Characteristics
    planet_name = forms.CharField(label="Planet Name", max_length=100)
    planet_temperature = forms.IntegerField(
        label="Temperature", min_value=-130, max_value=260
    )
    life_form = forms.ChoiceField(
        label="Select the Life Form",
        choices=[
            ("empty", "Empty"),
            ("human", "Human"),
            ("kaelesh", "Kaelesh"),
            ("rock_tal", "Rock'Tal"),
            ("mecha", "Mecha"),
        ],
    )
    galaxy = forms.IntegerField(label="Galaxy: ", min_value=1, max_value=9)
    system = forms.IntegerField(label="System: ", min_value=1, max_value=499)
    position = forms.IntegerField(label="Position: ", min_value=1, max_value=15)


class AccountTechnologyForm(forms.Form):
    # Techs:
    energy_technology = forms.IntegerField(
        label="Energy Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    laser_technology = forms.IntegerField(
        label="Laser Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    ion_technology = forms.IntegerField(
        label="Ion Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    hyperspace_technology = forms.IntegerField(
        label="Hyperspace Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    plasma_technology = forms.IntegerField(
        label="Plasma Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    combustion_drive = forms.IntegerField(
        label="Combustion Drive",
        initial=0,
        max_value=500,
        min_value=0,
    )
    impulsive_drive = forms.IntegerField(
        label="Impulsive Drive",
        initial=0,
        max_value=500,
        min_value=0,
    )
    hyperspace_drive = forms.IntegerField(
        label="Hyperspace Drive",
        initial=0,
        max_value=500,
        min_value=0,
    )
    espionage_technology = forms.IntegerField(
        label="Espionage Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    computer_technology = forms.IntegerField(
        label="Computer Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    astrophysics = forms.IntegerField(
        label="Astrophysics",
        initial=0,
        max_value=500,
        min_value=0,
    )
    intergalactic_research_network = forms.IntegerField(
        label="Intergalactic Research Network",
        initial=0,
        max_value=500,
        min_value=0,
    )
    graviton_technology = forms.IntegerField(
        label="Graviton",
        initial=0,
        max_value=500,
        min_value=0,
    )
    weapons_technology = forms.IntegerField(
        label="Weapons Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    shielding_technology = forms.IntegerField(
        label="Shielding Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )
    armour_technology = forms.IntegerField(
        label="Armour Technology",
        initial=0,
        max_value=500,
        min_value=0,
    )


class PlanetFacilitiesForm(forms.Form):
    # Facilites:
    robotics_factory = forms.IntegerField(
        label="Robotics Factory",
        initial=0,
        max_value=500,
        min_value=0,
    )
    nanite_factory = forms.IntegerField(
        label="Nanite Factory",
        initial=0,
        max_value=500,
        min_value=0,
    )
    research_lab = forms.IntegerField(
        label="Research Lab",
        initial=0,
        max_value=500,
        min_value=0,
    )
    shipyard = forms.IntegerField(
        label="ShipYard",
        initial=0,
        max_value=500,
        min_value=0,
    )


class PlanetBuildingsForm(forms.Form):
    # Buildings:
    metal_mine = forms.IntegerField(
        label="Metal Mine",
        initial=0,
        max_value=500,
        min_value=0,
    )
    crystal_mine = forms.IntegerField(
        label="Crystal Mine",
        initial=0,
        max_value=500,
        min_value=0,
    )
    deuterium_synthetizer = forms.IntegerField(
        label="Deuterium Synthetizer",
        initial=0,
        max_value=500,
        min_value=0,
    )
    solar_plant = forms.IntegerField(
        label="Solar Plant",
        initial=0,
        max_value=500,
        min_value=0,
    )
    fusion_plant = forms.IntegerField(
        label="Fusion Plant",
        initial=0,
        max_value=500,
        min_value=0,
    )


class PlanetAmplifiersForm(forms.Form):
    # Amplifiers:
    metal_amplifier = forms.ChoiceField(
        label="Select:",
        choices=[
            (0, "0"),
            (0.1, "10%"),
            (0.2, "20%"),
            (0.3, "30%"),
            (0.4, "40%"),
        ],
        initial=0,
    )
    crystal_amplifier = forms.ChoiceField(
        label="Select:",
        choices=[
            (0, "0%"),
            (0.1, "10%"),
            (0.2, "20%"),
            (0.3, "30%"),
            (0.4, "40%"),
        ],
        initial=0,
    )
    deuterium_amplifier = forms.ChoiceField(
        label="Select:",
        choices=[
            (0, "0%"),
            (0.1, "10%"),
            (0.2, "20%"),
            (0.3, "30%"),
            (0.4, "40%"),
        ],
        initial=0,
    )
    energy_amplifier = forms.ChoiceField(
        label="Select:",
        choices=[
            (0, "0%"),
            (0.2, "20%"),
            (0.4, "40%"),
            (0.6, "60%"),
            (0.8, "80%"),
        ],
        initial=0,
    )


class HumanBuildings(forms.Form):
    residential_sector = forms.IntegerField(
        label="Residential Sector: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    biosphere_farm = forms.IntegerField(
        label="Biosphere Farm: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    research_centre = forms.IntegerField(
        label="Research Centre: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    academy_sciences = forms.IntegerField(
        label="Academy of Sciences: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    neuro_calibration_centre = forms.IntegerField(
        label="Neuro-Calibration Centre: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    high_energy_smelting = forms.IntegerField(
        label="High Energy Smelting: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    food_silo = forms.IntegerField(
        label="Food Silo: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    fusion_powered_production = forms.IntegerField(
        label="Fusion-Powered Production: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    skycraper = forms.IntegerField(
        label="Skycraper: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    biotech_lab = forms.IntegerField(
        label="Biotech Lab: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    metropolis = forms.IntegerField(
        label="Metropolis: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    planetary_shield = forms.IntegerField(
        label="Planetary Shield: ",
        min_value=0,
        max_value=500,
        initial=0,
    )


class RocktalBuildings(forms.Form):
    meditation_enclave = forms.IntegerField(
        label="Meditation Enclave: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    crystal_farm = forms.IntegerField(
        label="Crystal Farm: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    rune_technologium = forms.IntegerField(
        label="Rune Technologium: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    rune_forge = forms.IntegerField(
        label="Rune Forge: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    oriktorium = forms.IntegerField(
        label="Oriktorium: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    magma_forge = forms.IntegerField(
        label="Magma Forge: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    disruption_chamber = forms.IntegerField(
        label="Disruption Chamber: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    monolith = forms.IntegerField(
        label="Monolith: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    crystal_refinery = forms.IntegerField(
        label="Crystal Refinery: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    deuterium_synthesiser = forms.IntegerField(
        label="Deuterium Synthesiser: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    mineral_research_center = forms.IntegerField(
        label="Mineral Research Center: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    advanced_recycling_plant = forms.IntegerField(
        label="Advanced Recycling Plant: ",
        min_value=0,
        max_value=500,
        initial=0,
    )


class KaeleshBuildings(forms.Form):
    sanctuary = forms.IntegerField(
        label="Sanctuary: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    antimatter_condenser = forms.IntegerField(
        label="Antimatter Condenser: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    vortex_chamber = forms.IntegerField(
        label="Vortex Chamber: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    halls_knowledge = forms.IntegerField(
        label="Halls of Knowledge: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    forum_transcendence = forms.IntegerField(
        label="Forum of Transcendence: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    antimatter_convector = forms.IntegerField(
        label="Antimatter Convector: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    cloning_laboratory = forms.IntegerField(
        label="Cloning Laboratory: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    chrysalis_accelerator = forms.IntegerField(
        label="Chrysalis Accelerator: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    bio_modifier = forms.IntegerField(
        label="Bio Modifier: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    psionic_modulator = forms.IntegerField(
        label="Psionic Modulator: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    ship_manufacturing_hall = forms.IntegerField(
        label="Ship Manufactoring Hall: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    supra_refractor = forms.IntegerField(
        label="Supra Refractor: ",
        min_value=0,
        max_value=500,
        initial=0,
    )


class MechasBuildings(forms.Form):
    sanctuary = forms.IntegerField(
        label="Sanctuary: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    antimatter_condenser = forms.IntegerField(
        label="Antimatter Condenser: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    vortex_chamber = forms.IntegerField(
        label="Vortex Chamber: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    halls_knowledge = forms.IntegerField(
        label="Halls of Knowledge: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    forum_transcendence = forms.IntegerField(
        label="Forum of Transcendence: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    antimatter_convector = forms.IntegerField(
        label="Antimatter Convector: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    cloning_laboratory = forms.IntegerField(
        label="Cloning Laboratory: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    chrysalis_accelerator = forms.IntegerField(
        label="Chrysalis Accelerator: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    bio_modifier = forms.IntegerField(
        label="Bio Modifier: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    psionic_modulator = forms.IntegerField(
        label="Psionic Modulator: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    ship_manufacturing_hall = forms.IntegerField(
        label="Ship Manufactoring Hall: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
    supra_refractor = forms.IntegerField(
        label="Supra Refractor: ",
        min_value=0,
        max_value=500,
        initial=0,
    )
