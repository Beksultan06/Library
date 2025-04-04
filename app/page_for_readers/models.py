from django.db import models
from ckeditor.fields import RichTextField

class Banner(models.Model):
    title = models.CharField(max_length=244, verbose_name='заголовок')
    description = RichTextField(verbose_name= 'описание')
    image = models.ImageField(verbose_name= 'фото')
    links = models.URLField(verbose_name = 'ссылка')

    class Meta:
        verbose_name = 'страница читателям'
        verbose_name_plural = 'страницы читателям'

    def __str__(self):
        return self.title
    
class Graphic_work(models.Model):
    title =  models.CharField(max_length=244, verbose_name='заголовок')
    description = RichTextField(verbose_name= 'описание')

    class Meta:
        verbose_name = 'страница читателям про график'
        verbose_name_plural = 'страницы читателям про график'

    def __str__(self):
        return self.title
    
class Titles(models.Model):
    work  = models.CharField(max_length=244, verbose_name='график работы')
    citizens = models.CharField(max_length=244, verbose_name='график приема граждан')
    hall =  models.CharField(max_length=244, verbose_name='зал читателей')
    readers =  models.CharField(max_length=244, verbose_name='рейтинг читателей')
    books =  models.CharField(max_length=244, verbose_name='рейтинг книг')

    class Meta:
        verbose_name = 'основные настройки страницы читателя'
        verbose_name_plural = 'основные настройки страницы читателей'

    def __str__(self):
        return self.work