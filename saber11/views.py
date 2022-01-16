from saber11.models import Colegio
from saber11.serializers import ColegioSerializer
from rest_framework import generics


class ColegioList(generics.ListCreateAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer


class ColegioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer
