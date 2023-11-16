from .models import Villain
from rest_framework import viewsets, serializers


class VillainViewSet(viewsets.ModelViewSet):
    class VillainSerializer(serializers.ModelSerializer):
        class Meta:
            model = Villain
            fields = ['name']

    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
