from django.contrib import admin

# Register your models here.
from location.models import Province, District, Ward


@admin.register(Province)
class ProvinceSite(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']


@admin.register(District)
class DistrictSite(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'province']


@admin.register(Ward)
class WardSite(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'district']
