from django.shortcuts import render
from django.views.generic import FormView

from .forms import (
    AccountCharacteristicsForm,
    PlanetCharacteristicsForm,
)

# Create your views here.


class EmpireSettingsView(FormView):
    template_name = "core/empire_settings_page.html"
    form_class = AccountCharacteristicsForm

    def form_valid(self, form):
        # We extract the number of planets sent by the user and we put it inside the session object.
        number_of_planets = form.cleaned_data["planet_count"]
        self.request.session["number_of_planets"] = number_of_planets

        # Let's create a list comprehension with the planets forms.
        planet_forms_list = [
            PlanetCharacteristicsForm(prefix=f"planet_{i}")
            for i in range(number_of_planets)
        ]

        # We return the render method, for   allowing the user to see what he sent.

        return render(
            request=self.request,
            template_name=self.template_name,
            context=self.get_context_data(
                form=form,
                planet_forms_list=planet_forms_list,
                number_of_planets=number_of_planets,
            ),
        )


def landing_page(request):
    return render(request, template_name="core/landing_page.html")


def index_view(request):
    visitor = request.session.keys()
    context = {"visitante": visitor}
    return render(request, template_name="core/index.html", context=context)
