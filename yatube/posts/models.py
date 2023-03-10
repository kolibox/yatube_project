from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.CharField(max_length=200)


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-pub_date']


'''
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    contact = models.EmailField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    location = models.CharField(max_length=400)
'''
