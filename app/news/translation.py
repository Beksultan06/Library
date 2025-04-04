from modeltranslation.translator import register, TranslationOptions
from app.news.models import *

@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(DailyNews)
class DailyNewsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'detailed_description')
    
@register(EventsNews)
class EventsNewsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'detailed_description', 'time')

@register(BookArrival)
class BookArrivalTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'author')

@register(MediaCoverage)
class MediaCoverageTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'coverage_period')