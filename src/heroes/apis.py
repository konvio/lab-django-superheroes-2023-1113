from rest_framework import viewsets, serializers

from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    class HeroSerializer(serializers.ModelSerializer):
        class Meta:
            model = Hero
            fields = "__all__"

    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
