from . import views
from django.urls import path
from .views import LandingPageView, HomePageView, NotificationsPageView, TemplateView, CreditPageView

urlpatterns = [
    path("", views.LandingPageView.as_view(), name = "landing"),
    path("home/", views.HomePageView.as_view(), name = "home"),
    path("notifications/", views.NotificationsPageView.as_view(), name = "notifications"),
    path("transit/", views.TransitPageView.as_view(), name = "transit"),
    path("credit/", views.CreditPageView.as_view(), name = "credit"),
]
