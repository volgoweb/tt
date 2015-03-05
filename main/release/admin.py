from django.contrib import admin
from .models import Release

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'date']

admin.site.register(Release, ReleaseAdmin)
