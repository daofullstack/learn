from django.apps import AppConfig


class SentinelappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sentinelapp"

    def ready(self):
        from .auto import updater

        updater.start()
