from django.urls import path

from .views import welcome_view

app_name = "landing"
urlpatterns = [
    path(route="", view=welcome_view, name="welcome_page"),
]
