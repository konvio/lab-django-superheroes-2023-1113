from django.contrib import admin
from .models import Villain


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    pass
