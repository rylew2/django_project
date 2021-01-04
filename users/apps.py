from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # django recommends doing this way to avoid side effects
    def ready(self):
        import users.signals