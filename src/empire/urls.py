from django.urls import include, path
from rest_framework import routers

from empire import views

router = routers.DefaultRouter()
router.register(r"planets", views.PlanetViewSet)
router.register(r"profiles", views.ProfileViewSet)
router.register(r"buildings", views.BuildingViewSet)
router.register(r"technologies", views.TechnologyViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
