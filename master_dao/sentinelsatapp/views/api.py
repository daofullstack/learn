from rest_framework import viewsets, mixins
from rest_framework.response import Response
from sentinelsatapp.serializers import PropertieSerializer
from sentinelsatapp.models import Propertie
from rest_framework.permissions import IsAuthenticated


class PropertieViewSet(viewsets.ModelViewSet):
    """
    Viewset for Propertie model.
    """

    serializer_class = PropertieSerializer
    queryset = Propertie.objects.all()
