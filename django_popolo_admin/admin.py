from django.contrib import admin
from popolo.models import Person

@admin.register(Person)
class ModelAdmin(admin.ModelAdmin):
    pass

