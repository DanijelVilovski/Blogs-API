from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        } 

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        } 