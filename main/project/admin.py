from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Project._meta.fields]

admin.site.register(Project, ProjectAdmin);
