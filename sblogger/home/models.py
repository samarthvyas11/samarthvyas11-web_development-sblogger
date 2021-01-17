from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField( primary_key=True)
    name = models.CharField(max_length=255,default="")
    phone = models.CharField(max_length=13,default="")
    email = models.CharField(max_length=100,default="")
    content = models.TextField(default="")
    timeStamp = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return " Message from " + str(self.name)

        
