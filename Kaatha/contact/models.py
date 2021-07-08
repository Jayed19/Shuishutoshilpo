from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    msg = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    