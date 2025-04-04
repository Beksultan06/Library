from django.contrib import admin
from app.base.models import Logo, Catalogs_ElectronicLibrary, WeOfferViewing, Partners, ReadingRating, BooksRating, PartnerImage, LogoImage
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from app.base.translation import *

# Register your models here.

#Саидахмад

class LogoImageInline(admin.TabularInline):  # Или admin.StackedInline
    model = LogoImage
    extra = 3  # Показывает 3 пустые формы для загрузки новых фото
    fields = ("image", "image_preview")  # Добавляем миниатюру в админку
    readonly_fields = ("image_preview",)  # Миниатюры нельзя редактировать

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit:cover;" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью"

class LogoAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {"fields": ("title_ru",)}),
        ("Кыргызская версия", {"fields": ("title_ky",)}),
    )

    inlines = [LogoImageInline]  # Добавляем Inline для загрузки нескольких фото

    list_display = ("title_ru", "preview_images")
    
    def preview_images(self, obj):
        images = obj.logo_images.all()[:3]  # Показываем до 3 изображений в списке
        if images:
            return format_html(
                "".join(f'<img src="{img.image.url}" width="50" height="50" style="margin-right:5px;"/>' for img in images)
            )
        return "Нет изображений"

    preview_images.short_description = "Превью"

admin.site.register(Logo, LogoAdmin)


class Catalogs_ElectronicLibrary_Admin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
    )
admin.site.register(Catalogs_ElectronicLibrary, Catalogs_ElectronicLibrary_Admin)



#Алишер
class WeOfferViewingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru','selections_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky','selections_ky', 'description_ky')
        }),
       
    )
admin.site.register(WeOfferViewing, WeOfferViewingAdmin)




class PartnerImageInline(admin.TabularInline):
    model = PartnerImage
    extra = 3
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit:cover;" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью"


class PartnersAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {"fields": ("title_ru",)}),
        ("Кыргызская версия", {"fields": ("title_ky",)}),
    )

    inlines = [PartnerImageInline]

    list_display = ("title_ru", "preview_images")

    def preview_images(self, obj):
        images = obj.partner_images.all()[:3]
        if images:
            return format_html(
                "".join(f'<img src="{img.image.url}" width="50" height="50" style="margin-right:5px;"/>' for img in images)
            )
        return "Нет изображений"

    preview_images.short_description = "Превью"

admin.site.register(Partners, PartnersAdmin)

  
class ReadingRatingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'place_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'place_ky', 'description_ky')
        }),
     
    )
admin.site.register(ReadingRating, ReadingRatingAdmin)   

  
class BooksRatingAdmin(TranslationAdmin):
    fieldsets = (
        ("Русская версия", {
            'fields': ('title_ru', 'place_ru', 'description_ru')
        }),
        ("Кыргызская версия", {
            'fields': ('title_ky', 'place_ky', 'description_ky')
        }),
      
    )
admin.site.register(BooksRating, BooksRatingAdmin)

