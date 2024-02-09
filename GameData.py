import data


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
