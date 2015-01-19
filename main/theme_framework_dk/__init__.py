from django.conf import settings

settings.INSTALLED_APPS += (
    'main.theme_framework_dk.base',
    'main.theme_framework_dk.fotorama',
    'main.theme_framework_dk.detail',
    'main.theme_framework_dk.field',
    'main.theme_framework_dk.list',
    'main.theme_framework_dk.block',
    'main.theme_framework_dk.pagination',
)
