from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.name


class Grant(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='related_location')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='related_discipline')
    duration = models.CharField(max_length=128, blank=True, null=True)
    deadline = models.CharField(max_length=128, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='related_category')
    img = models.ImageField(upload_to='media/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Возможность'
        verbose_name_plural = 'Возможности'

    def __str__(self):
        return self.name