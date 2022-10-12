from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homeview'),
    path('blogs/<int:pk>', views.BlogsDetailView.as_view(), name='blogdetailview'),
    path('addblog', views.AddBlogView.as_view(), name='addblogview'),
    path('blogs/updateblog/<int:pk>', views.EditBlogView.as_view(), name='updateblogview'),
    path('blogs/<int:pk>/deleteblog', views.DeleteBlogView.as_view(), name='deleteblogview'),

    path('addcategory', views.AddCategoryView.as_view(), name='addcategoryview'),
    path('categories', views.CategoryView.as_view(), name='categoriesviews'),
    path('categories/editcategory/<int:pk>', views.EditCategoryView.as_view(), name='editcategoryview'),
    path('categories/<int:pk>/deletecategory', views.DeleteCategoryView.as_view(), name='deletecategoryview'),
    re_path('category/(?P<categoryname>[-\w]*)/$', views.CategoryBlogList, name='category'),

    path('likeblog/<int:pk>', views.LikeBlogView, name='like_blog'),

    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),

    path('author', views.AuthorView.as_view(), name='authorview'),
]