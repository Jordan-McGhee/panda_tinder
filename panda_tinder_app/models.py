from django.db import models

# Create your models here.
class Panda(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    favorite_food = models.CharField(max_length=255)
    knows_kungfu = models.BooleanField()
    #dates > many to many
    #posts > one to many
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# One to Many
class Date(models.Model):
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    location = models.CharField(max_length=255)
    
    # Many to Many
    pandas_on_date = models.ManyToManyField(Panda, related_name = "dates")

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Panda, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)