from modeltranslation.translator import TranslationOptions, register
from app.professional_activity.models import Activity


@register(Activity)
class ActivityTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
        'description_details'
    )
