from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Телефонный номер"
    )
        