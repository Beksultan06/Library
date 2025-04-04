from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from django.core.exceptions import ValidationError


#Абстрак
class User(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    CATEGORY_CHOICES = [
        ('student', 'Студент'),
        ('schoolboy', 'Школьник'),
        ('pensioner', 'Пенсионер'),
        ('employee', 'Служащий'),
        ('SEN', 'ОВЗ, ограниченные возможности здоровья'),
        ('Other', 'Другое'),
    ]

    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Пол"
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта"
    )

    def validate_phone_number(value):
        pattern = r'^\+996\d{9}$'
        if not re.match(pattern, value):
            raise ValidationError("Номер телефона должен быть в формате +996XXXXXXXXX")

    phone = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_phone_number],
        verbose_name="Номер телефона"
    )

    reitforusers = models.PositiveIntegerField(
        default=0,
        verbose_name="Рейтинг пользователя"
    )

    image =  models.ImageField(verbose_name = 'фото', upload_to= 'users')

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.full_name
        super().save(*args, **kwargs)


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"


