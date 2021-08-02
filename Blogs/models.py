from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    full_content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    published_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now= True)


    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title
