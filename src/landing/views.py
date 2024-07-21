from django.shortcuts import render

# Create your views here.


def welcome_view(request):
    return render(request=request, template_name="landing/welcome.html")
