from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog 
from .forms import BlogForm

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

class AddBlogView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'addblog.html'
    #fields = '__all__'

