from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from .forms import AccountCharacteristicsForm

# Create your views here.


class EmpireSettingsView(FormView):
    template_name = "core/empire_settings_page.html"
    form_class = AccountCharacteristicsForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        context = self.get_context_data()
        return render(
            request=request,
            template_name=self.template_name,
            context=context,
        )


def landing_page(request):
    return render(request, template_name="core/landing_page.html")
