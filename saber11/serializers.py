from rest_framework import serializers
from saber11.models import Colegio

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = '__all__'
