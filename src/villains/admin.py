from django.contrib import admin
from src.villains.models import Villain


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    pass
