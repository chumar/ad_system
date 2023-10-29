from django.contrib import admin
from .models import Ad,Location,CreateUser,UserVisit,FileStored

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('ad_name', 'start_date', 'end_date', 'get_location_names')

    def get_location_names(self, obj):
        return ", ".join([location.name for location in obj.locations.all()])

    get_location_names.short_description = 'Locations'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_daily_visitors')

@admin.register(CreateUser)
class UserCreationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')

admin.site.register(UserVisit)
admin.site.register(FileStored)
