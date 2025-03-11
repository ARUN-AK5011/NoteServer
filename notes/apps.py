from django.apps import AppConfig

class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'

    def ready(self):
        from django.db.models.signals import pre_migrate
        pre_migrate.disconnect(dispatch_uid="disable_migrations")
