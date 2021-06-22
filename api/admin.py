from django.contrib import admin
from .models import CBU


@admin.register(CBU)
class CBUModelAdmin(admin.ModelAdmin):
    pass
