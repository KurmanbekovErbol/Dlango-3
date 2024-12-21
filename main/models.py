from django.db import models

# Create your models here.
class Banners(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изобажение'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главное"
        verbose_name_plural = "Главное"