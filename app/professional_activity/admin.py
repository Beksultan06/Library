from django.contrib import admin
from app.professional_activity.models import Activity
from modeltranslation.admin import TranslationAdmin
from .translations import *


class ActivityAdmin(TranslationAdmin):
    fieldsets = ( 
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru', 'description_details_ru', 'links'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky', 'description_details_ky'],
        }),
    )

admin.site.register(Activity, ActivityAdmin)
