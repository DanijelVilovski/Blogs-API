from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blogs/<int:pk>', views.BlogsDetailView.as_view(), name='blogdetailview')
]