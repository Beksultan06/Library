from django.contrib import admin
from app.page_for_readers.models import Banner, Graphic_work, Titles
from modeltranslation.admin import TranslationAdmin
from .translations import *

class BannerAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Основа', {
            'fields': ['image', 'links'],
        }),
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', ],
        }),
    )

admin.site.register(Banner, BannerAdmin)

class Graphic_workAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', ],
        }),
    )

admin.site.register(Graphic_work, Graphic_workAdmin)

class TitlesAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['work_ru', 'citizens_ru', 'hall_ru', 'readers_ru', 'books_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['work_ky', 'citizens_ky', 'hall_ky', 'readers_ky', 'books_ky' ],
        }),
    )

admin.site.register(Titles, TitlesAdmin)

