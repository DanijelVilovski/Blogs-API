from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Blog, Category 
from .forms import AddBlogForm, EditBlogForm, AddCategoryForm, EditCategoryForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# listview allows us to  list a query set into the database (all blog posts)
# detailview is similar but it brings back details of just one record (one blog post)

# Create your views here.

#class based views

class HomeView(ListView):
    model = Blog
    template_name = 'home.html'
    # ordering = ['-id'] #we want the last added or updated blog, to be positioned on top of the list of blogs 
    ordering = ['-date_created']

class BlogsDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class AddBlogView(CreateView):
    model = Blog
    form_class = AddBlogForm
    template_name = 'addblog.html'
    #fields = '__all__'

    #a method that allows adding a blog without specifying the author, and automatically making the 
    #logged-in user the author of the new blog
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditBlogView(UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'updateblog.html'
    #fields = ['title', 'body']

class DeleteBlogView(DeleteView):
    model = Blog
    success_url = 'http://localhost:8000'
    template_name = "deleteblog.html"

class CategoryView(ListView):
    model = Category
    template_name = 'categories.html'

class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'addcategory.html'

class EditCategoryView(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'updatecategory.html'

class DeleteCategoryView(DeleteView):
    model = Category
    success_url = 'http://localhost:8000/categories'
    template_name = "deletecategory.html"

class AuthorView(ListView):
    model = Blog
    template_name = "author.html"

#functions based views

def CategoryBlogList(request, categoryname):
    category = Category.objects.get(name=categoryname) 
    category_blogs = Blog.objects.filter(category=category)
    return render(request, 'category.html', {'cats': categoryname, 'category_blogs': category_blogs})

def LikeBlogView(request, pk):
    blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))
    liked = False

    if blog.likes.filter(id=request.user.id).exists():
        blog.likes.remove(request.user)
        liked = False
    else: 
        blog.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blogdetailview', args=[str(pk)]))

    

