from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "project.apps.core"

    def ready(self):
        import project.apps.core.signals
