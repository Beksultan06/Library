from modeltranslation.translator import TranslationOptions, register
from app.page_for_readers.models import Banner, Graphic_work, Titles


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )
@register(Graphic_work)
class Graphic_for_workTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )
@register(Titles)
class TitlesTranslationOptions(TranslationOptions):
    fields = (
        "work",
        "citizens",
        "hall",
        'readers',
        'books'
    )







