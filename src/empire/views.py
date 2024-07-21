from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Building, Planet, Profile, Technology
from .serializers import (
    BuildingSerializer,
    PlanetSerializer,
    ProfileSerializer,
    TechnologySerializer,
)


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=True, methods=["get"])
    def planets(self, request, pk=None):
        profile = self.get_object()
        planets = Planet.objects.filter(profile=profile)
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
