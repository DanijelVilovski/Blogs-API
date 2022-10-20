from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy 
from django.contrib.auth.models import User
from blogs.models import Profile
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, EditProfileForm, EditBioForm, AddBioForm
from django.http import HttpResponse

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(DetailView):
    model = User
    template_name = 'registration/profile.html'

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('homeview')

class AddBioView(CreateView):
    form_class = AddBioForm
    template_name = 'registration/addbio.html'
    success_url = reverse_lazy('homeview')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditBioView(UpdateView):
    model = Profile
    form_class = EditBioForm
    template_name = 'registration/editbio.html'
    #success_url = reverse_lazy('homeview')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.id })
