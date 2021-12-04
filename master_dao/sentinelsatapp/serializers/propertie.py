from rest_framework import serializers
from sentinelsatapp.models import Propertie


class PropertieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertie
        fields = "__all__"
