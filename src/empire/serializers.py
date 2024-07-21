from rest_framework import serializers

from .models import Building, Planet, Profile, Technology


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class ProfileWithPlanetsSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True, read_only=True, source="planet_set")

    class Meta:
        model = Profile
        fields = ["id", "user", "name", "account_class", "universe_speed", "planets"]
