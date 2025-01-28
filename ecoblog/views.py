from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ProtectedArea


class HomeView(TemplateView):
    template_name = "ecoblog/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["natural_monuments"] = ProtectedArea.objects.filter(category__name="Monumento natural")
        context["national_parks"] = ProtectedArea.objects.filter(category__name="Parque nacional")
        
        return context
    

