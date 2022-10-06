from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homeview'),
    path('blogs/<int:pk>', views.BlogsDetailView.as_view(), name='blogdetailview'),
    path('addblog', views.AddBlogView.as_view(), name='addblogview'),
    path('blogs/updateblog/<int:pk>', views.EditBlogView.as_view(), name='updateblogview')
]