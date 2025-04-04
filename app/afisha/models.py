from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Afisha(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', help_text='Объявление о мероприятиях')
    image = models.ImageField(verbose_name='Изображение', upload_to='afisha/')
    description = RichTextField(verbose_name='Описание', help_text='Описание библиотеки')

    title_2 = models.CharField(max_length=255, verbose_name='Заголовок о мероприятиях')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление о мероприятиях"
        verbose_name_plural = "Объявления о мероприятиях"

class Events(models.Model):
    time_of_the_event = models.CharField(max_length=255, verbose_name='Время проведения мероприятия')
    title = models.CharField(max_length=255, verbose_name='Заголовок мероприятия')
    description = RichTextField(verbose_name='Описание мероприятия')
    image = models.ImageField(verbose_name='Изображение к мероприятию', upload_to='afisha/')
    details_link =models.URLField(verbose_name='Ссылка на "подробнее"', max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
