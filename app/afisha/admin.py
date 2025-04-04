from django.contrib import admin
from .models import Afisha, Events
from modeltranslation.admin import TranslationAdmin
from .translation import *

# Register your models here.
@admin.register(Afisha)
class AfishaAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображение', {
            'fields': ['image',],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'title_2_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'title_2_ky'],
        }),
    )

@admin.register(Events)
class EventsAdmin(TranslationAdmin):
    fieldsets = (
        ('Изображение', {
            'fields': ['image',],
        }),
        ('Русская версия', {
            'fields': ['time_of_the_event_ru','title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['time_of_the_event_ky', 'title_ky', 'description_ky'],
        }),
    )