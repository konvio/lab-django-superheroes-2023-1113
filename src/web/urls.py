from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from heroes.apis import HeroViewSet
from villains.apis import VillainViewSet

router = routers.DefaultRouter()
router.register(r"heroes", HeroViewSet)
router.register(r"villains", VillainViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("schema/", get_schema_view(title="Superhero API", version="1.0.0")),
]
