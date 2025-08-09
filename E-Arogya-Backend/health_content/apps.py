"""
App configuration for health_content
"""
from django.apps import AppConfig


class HealthContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'health_content'
    verbose_name = 'Health Content Management'
