from django.db import models

# Create your models here.
class registrationpage(models.Model):
    name=models.CharField(max_length=50,blank=False, null=False)
    pic=models.ImageField(upload_to='registrationPic/',blank=False, null=False)

    def __str__(self):
        return self.name
    