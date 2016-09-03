from django.db import models


class Paintings(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)


class GraphicDesign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)


class CharityDesign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    image = models.ImageField(null=True)
