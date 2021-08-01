from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models import Count
# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=150, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=50)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(max_length=5000)
    pub_date = models.DateField(default=now())
    likes = models.ManyToManyField(User, related_name='blogpost')
    header_image = models.ImageField(null = True, blank = True, upload_to = "blog/images")

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blogHome')

class Category(models.Model):
    name = models.CharField(max_length=150, default=" ")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogHome')

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

