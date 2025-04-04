from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

#Саидахмад
class Logo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = RichTextField(
        verbose_name="Описание"
    )

    library = models.CharField(
        max_length=255,
        verbose_name="Название библиотеки"
    )

    adress = models.CharField(
        max_length=255,
        verbose_name="Адресс"
    )

    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )

    logo = models.ImageField(
        upload_to="logos/",
        verbose_name="Логотип"
    )

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главные"


class LogoImage(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, related_name="logo_images")
    image = models.ImageField(upload_to="logo_images/", verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.logo.title}"

    class Meta:
        verbose_name = "Изображение логов"
        verbose_name_plural = "Изображения лого"



class Catalogs_ElectronicLibrary(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    description = RichTextField(
        verbose_name="Описание"
    )

    link = models.URLField(
        verbose_name="Ссылка на подробнее"
    )


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Каталог/Электронная библиотека"
        verbose_name_plural = "Каталоги/Электронные библиотеки"



#Алишер
class WeOfferViewing(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )

    selections = models.CharField(
        max_length=255,
        verbose_name='Подборка для вас'
    )

    description = RichTextField(
        verbose_name='Описание'
    )
    
    video_file = models.FileField(
        upload_to='videos/',
        null=True,  
        blank=True,
        verbose_name='Видео'
        )
        
    link = models.URLField(
        verbose_name='Ссылка на поподробнее',
        null=True,  
        blank=True 
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Предлагаем к Просмотру"
        verbose_name_plural = "Предлогают к просмотру"
        
        
class Partners(models.Model): 
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )    
    
    images = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Картинки партнёров'
    )
    
    
    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class PartnerImage(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, related_name="partner_images")
    image = models.ImageField(upload_to="partners_images/", verbose_name="Изображение")

    def __str__(self):
        return f"Изображение для {self.partner.title}"

    class Meta:
        verbose_name = "Изображение партнёра"
        verbose_name_plural = "Изображения партнёров"
        
        
        
class ReadingRating(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Рейтинг читателей(ТОП-3)'
    )

    place = models.CharField(
        max_length=255,
        verbose_name='Место'
    )

    description = RichTextField(
        verbose_name='Рейтинг читателя'
    )

    images = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Фото читателя'
    )


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Рейтинг читателя"
        verbose_name_plural = "Рейтинг читателей"
        

class BooksRating(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Рейтинг книг(ТОП-3)'
    )

    place = models.CharField(
        max_length=255,
        verbose_name='Место'
    )

    description = RichTextField(
        verbose_name='Книга'
    )

    images = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name='Фото книги'
    )


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Рейтинг книги"
        verbose_name_plural = "Рейтинг книг"
