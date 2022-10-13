from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),

    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/editprofile', views.UserEditView.as_view(), name='editprofile'),
    path('profile/<int:pk>/editprofile/password', views.PasswordChangeView.as_view(), name='passwordchange')
]