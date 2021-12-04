from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from sentinelsatapp.views import PropertieViewSet, home, load_sentinel


"""
Mise en place des routers de l'application Common
"""
rooter = routers.DefaultRouter()

rooter.register("propertie", PropertieViewSet, basename="propertie")


urlpatterns = [
    path("api/", include(rooter.urls)),
    path("", home, name="home-page"),
    path("load_sentinel", load_sentinel, name="load_sentinel"),
]
