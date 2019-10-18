from django.db import models

class blog(models.Model):
    tital = models.TextField(max_length=80)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="image/")


    def __str__(self):
        return self.tital

    def summary(self):
        return self.body[:100]

    def date(self):
        return self.pub_date.strftime('%b %e %Y')