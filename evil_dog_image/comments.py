from django.db import models

from evil_dog_image.models import Paintings, GraphicDesign, CharityDesign


class Likes(models.Model):
    paintings = models.ForeignKey(Paintings, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name="paintings")
    graphics = models.ForeignKey(GraphicDesign, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="graphic")
    charity = models.ForeignKey(CharityDesign, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name="charity")
    facebook_user = models.CharField(max_length=200)
    likes_url = models.TextField()
    user_profile = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")

    class Meta:
        ordering = ['-datetime']
