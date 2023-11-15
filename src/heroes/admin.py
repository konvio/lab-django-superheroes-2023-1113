from django.contrib import admin
from src.heroes.models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass
