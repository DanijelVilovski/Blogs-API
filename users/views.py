from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy 
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.http import HttpResponse

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# def LoginView(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         user.is_active = True
#         login(request, user)
#         return render(request, 'login.html')
#     else:
#         return HttpResponse("Nesto nije u redu")


# def LogoutView(request):
#     logout(request)
#     return HttpResponse("Sve u redu batice")
   