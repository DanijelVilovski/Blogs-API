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
    header_image = models.ImageField(blank=True, null=True, upload_to="images/") # images is folder inside media folder
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


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length= 500, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user) 

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s ' % (self.blog.title) 