from django.apps import AppConfig


class AppCantinhoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_cantinho'

    def ready(self):
        import app_cantinho.signals