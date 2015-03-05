from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'next_release']

admin.site.register(Project, ProjectAdmin);
