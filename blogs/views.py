from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Blog 

# listview allows us to  list a query set into the database (all blog posts)
# detailview is similar but it brings back details of just one record (one blog post)

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogsDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

