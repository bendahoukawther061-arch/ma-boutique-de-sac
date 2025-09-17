from django.contrib import admin
from .models import Sac

@admin.register(Sac)
class SacAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom', 'description')
  