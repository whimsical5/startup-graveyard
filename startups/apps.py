from django.apps import AppConfig
import os

class StartupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'startups'

    def ready(self):
        if os.environ.get('RUN_MIGRATE_ON_DEPLOY') == 'true':
            from django.core.management import call_command
            from django.contrib.auth import get_user_model

            try:
                call_command('migrate')
                call_command('collectstatic', interactive=False, verbosity=0)

                User = get_user_model()
                if not User.objects.filter(username='admin').exists():
                    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword123')
            except Exception as e:
                print("Migration error:", e)
