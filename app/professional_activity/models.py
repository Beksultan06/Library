from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=255, verbose_name= 'заголовок',unique=True)
    description = RichTextField(verbose_name = 'описание')
    links = models.CharField(max_length=355,verbose_name='Ссылка')
    description_details = RichTextField(verbose_name = "детальное описание")
    class Meta:
        verbose_name = 'профессиональная деятельность'
        verbose_name_plural = 'профессиональная деятельности'

    def __str__(self):
        return self.title