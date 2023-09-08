from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField("name", max_length=50)
    image = models.ImageField(null = True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name