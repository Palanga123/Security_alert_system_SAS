from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = "index.html"

class HomePageView(TemplateView):
    template_name = "home.html"
    
class NotificationsPageView(TemplateView):
    template_name = "notifications.html"

class TransitPageView(TemplateView):
    template_name = "transit.html"

class CreditPageView(TemplateView):
    template_name = "credit.html"

