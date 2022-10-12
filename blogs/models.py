from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('categoriesviews')

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=500, default='Click on the blog to see more details!')
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + " | " + str(self.author) # parsing to string because author is object

    def get_absolute_url(self):
        return reverse('blogdetailview', args=[str(self.id)]) #method where we define where to redirect after adding blog 