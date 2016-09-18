from django.db import models


class Paintings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")


class GraphicDesign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")


class CharityDesign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")
