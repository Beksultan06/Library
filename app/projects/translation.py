from modeltranslation.translator import register, TranslationOptions
from .models import OurProjects, MainProjects, AmericanCorner

@register(OurProjects)
class OurProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(MainProjects)
class MainProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(AmericanCorner)
class AmericanCornerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')