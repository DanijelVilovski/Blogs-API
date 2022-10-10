from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.author) # parsing to string because author is object

    def get_absolute_url(self):
        return reverse('blogdetailview', args=[str(self.id)]) #method where we define where to redirect after adding blog 