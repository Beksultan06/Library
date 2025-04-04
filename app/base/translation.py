from modeltranslation.translator import register, TranslationOptions
from app.base.models import Logo, Catalogs_ElectronicLibrary, WeOfferViewing, Partners, ReadingRating, BooksRating


#Саидахмад
@register(Logo)
class LogoTranslation(TranslationOptions):
    fields = ('title', 'description', 'library')


@register(Catalogs_ElectronicLibrary)
class Catalogs_ElectronicLibrary_Translation(TranslationOptions):
    fields = ('title', 'description')


#Алишер
@register(WeOfferViewing)
class WeOfferViewingTranslation(TranslationOptions):
    fields = ('title', 'selections', 'description' )


@register(Partners)
class PartnersTranslation(TranslationOptions):
    fields = ('title',)


@register(ReadingRating)
class ReadingRatingTranslation(TranslationOptions):
    fields = ('title', 'place', 'description')
    

@register(BooksRating)
class BooksRatingTranslation(TranslationOptions):
    fields = ('title', 'place', 'description')
