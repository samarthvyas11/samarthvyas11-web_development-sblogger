from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField( primary_key=True,auto_created=True)
    title = models.CharField(max_length=255,default="")
    author = models.CharField(max_length=13,default="")
    email = models.CharField(max_length=100,default="")
    slug = models.SlugField(max_length=100,default="")
    content = models.TextField(default="")
    timeStamp = models.DateTimeField(blank=True,default=now)
    



    def __str__(self):
        return str(self.title) + " by " + str(self.author)
class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True,auto_created=True)
    comment = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)


    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username