from django.contrib import admin
from popolo.models import Person, Organization

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
