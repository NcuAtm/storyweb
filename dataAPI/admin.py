from django.contrib import admin
from .models import AeroboxData, Aerobox, ProjectData, UserExtension

class AeroboxDataAdmin(admin.ModelAdmin):
    list_display=('id', 'pm', 'temp', 'rh', 'co2', 'lon', 'lat', 'time')

class AeroboxAdmin(admin.ModelAdmin):
    list_display=('id', 'aerobox_id', 'sitename')#, 'aeroboxdata')

class ProjectDataAdmin(admin.ModelAdmin):
    list_display=('id', 'pj_name', 'start_time', 'end_time')#, 'aerobox')

class UserExtensionAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'u_name', 'personal_key')#, 'projectdata')

admin.site.register(AeroboxData, AeroboxDataAdmin)
admin.site.register(Aerobox, AeroboxAdmin)
admin.site.register(ProjectData, ProjectDataAdmin)
admin.site.register(UserExtension, UserExtensionAdmin)

