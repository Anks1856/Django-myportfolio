from django.db import models

class myprofile(models.Model):
    image = models.ImageField(upload_to="image/")
    summary = models.TextField(max_length=200)



