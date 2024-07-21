from django.forms import ModelForm, Select, TextInput

from empire.models import AccountUserSettingDb, PlanetDb

widget_class = (
    "input bg-slate-800 border border-gray-700 rounded-lg p-2 text-white w-full"
)


class AccountSettingsForm(ModelForm):
    class Meta:
        model = AccountUserSettingDb

        exclude = ["user_fk", "id"]
        widgets = {
            "universe_economy": TextInput(attrs={"class": widget_class}),
            "account_class": Select(attrs={"class": widget_class}),
        }


class PlanetForm(ModelForm):
    class Meta:
        model = PlanetDb

        exclude = ["account_fk", "id"]
        widgets = {
            "planet_name": TextInput(attrs={"class": widget_class}),
            "planet_temperature": TextInput(attrs={"class": widget_class}),
            "planet_galaxy": TextInput(attrs={"class": widget_class}),
            "planet_system": TextInput(attrs={"class": widget_class}),
            "planet_position": TextInput(attrs={"class": widget_class}),
        }
