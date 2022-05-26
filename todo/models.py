from distutils.command.upload import upload
from re import T
from turtle import title
from unicodedata import category
from django.db import models
from accounts.models import User
# Create your models here.

# Todo Model 
class Todo(models.Model):
    STATUS_CHOICES = (
        ('t', 'تکمیل شده'),
        ('m', 'موکول شده'),
        ('l', 'لغو شده'),
        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='Todo', blank=True, null=True)
    end_time = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


# Category Model 
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Note(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

class Voice(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    voice = models.FileField(upload_to='VoiceAttachment')



class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class WhereIsIt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title





