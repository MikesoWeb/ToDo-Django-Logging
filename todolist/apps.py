from django.apps import AppConfig


class TodolistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todolist'

    def ready(self):
        # Не используйте "todoapp.log_settings", так как файл лежит в корневой папке
        pass
