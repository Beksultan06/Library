from modeltranslation.translator import TranslationOptions, register

from .models import *

@register(Afisha)
class AfishaTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'title_2')

@register(Events)
class EventsTranslationOptions(TranslationOptions):
    fields = ( 'time_of_the_event', 'title', 'description')



