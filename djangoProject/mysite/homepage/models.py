from django.db import models

# Create your models here.

class ImgTable(models.Model):
    image = models.FileField(null=True, upload_to='images_dir/')

    def __str__(self):
        return str(self.image)

# class Image(models.Model):
#     image = models.ForeignKey(ImgTable, on_delete = models.CASCADE)

# class image(models.Model):
#     img = models.ImageField(upload_to=filepath, null=True, blank=True)