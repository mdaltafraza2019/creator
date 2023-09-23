from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File(models.Model):
    docoument_name=models.CharField(max_length=100)
    document=models.FileField(upload_to='media/')
    usern=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.docoument_name
