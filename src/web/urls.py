from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from heroes.apis import HeroViewSet
from villains.apis import VillainViewSet

router = routers.DefaultRouter()
router.register(r"heroes", HeroViewSet)
router.register(r"villains", VillainViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
