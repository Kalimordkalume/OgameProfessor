from django.urls import path

from .views import EmpireSettingsView, index_view, landing_page

app_name = "core"
urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("empire_settings", EmpireSettingsView.as_view(), name="empire_page"),
    path("index", index_view, name="index_page"),
]
