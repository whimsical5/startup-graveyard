from django.apps import AppConfig
import os

class StartupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'startups'

    def ready(self):
        if os.environ.get('RUN_MIGRATE_ON_DEPLOY') == 'true':
            from django.core.management import call_command
            try:
                call_command('migrate')
                call_command('collectstatic', interactive=False, verbosity=0)
            except Exception as e:
                print("Migration error:", e)
