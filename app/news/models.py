from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок страницы "Новости"'
    )
    description = RichTextField(
        verbose_name='Описание библиотеки'
    )
    left_image = models.ImageField(
        upload_to='left-image/',
        verbose_name='Левое изображение'
    )
    middle_image = models.ImageField(
        upload_to='middle-image/',
        verbose_name='среднее изображение'
    )
    dextral_image = models.ImageField(
        upload_to='dextral-image/',
        verbose_name='Правое изображение'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class DailyNews(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок дневных новостей'
    )
    description = RichTextField(
        verbose_name="Описание дневных новостей"
    )
    detailed_description = RichTextField(
        verbose_name="Подробное описание"
    )
    image = models.ImageField(
        upload_to='daily-news-image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Дневную новость'
        verbose_name_plural = 'Дневные новости'

class EventsNews(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок мероприятия'
    )
    description = RichTextField(
        verbose_name="Описание мероприятия"
    )
    detailed_description = RichTextField(
        verbose_name="Подробное описание"
    )
    image = models.ImageField(
        upload_to='events-image/',
        verbose_name='Изображение'
    )
    time = models.CharField(
        max_length=255,
        verbose_name='Время проведения мероприятия'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
    

class BookArrival(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = RichTextField(verbose_name="Описание")
    image = models.ImageField(upload_to='book_arrival_images/', verbose_name="Изображение")
    link = models.URLField(verbose_name="Ссылка")
    file = models.FileField(upload_to='files/', verbose_name="Файл")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Прибытие книги"
        verbose_name_plural = "Прибытие книг"

class MediaCoverage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    coverage_period = models.CharField(max_length=250, verbose_name="Период охвата")
    description = RichTextField(verbose_name="Описание")
    link = models.URLField(verbose_name="Ссылка")
    image = models.ImageField(upload_to='media_coverage_images/', verbose_name="Изображение")
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Освещение в СМИ"
        verbose_name_plural = "Освещения в СМИ"