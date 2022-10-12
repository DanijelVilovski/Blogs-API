from django import forms
from .models import Blog, Category

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'snippet','body']
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        } 

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'snippet','body']  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        } 

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        } 

class EditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        } 