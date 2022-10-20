# Blogs Website

Checkout my website on Heroku: https://danijels-blog-website.herokuapp.com/

This website is fully written using Django.

## Libraries used

- Pillow - for images
- Bootstrap - for styling
- Ckeditor - for rich text editor
- Psycopg2 - Adapter for PostgreSQL database

## Functionalities

#### User
    - registration, 
    - login, 
    - logout,
    - edit profile,
    - edit bio

#### Blog
    - add,
    - edit,
    - delete,
    - like/unlike blog,
    - comment on blogs,
    - list blogs by the category
    - paggination

#### Admin
    - Only admin can add, update, or delete categories 
    - Admin is the person whose field 'is_superuser' is True 

#### More about website
    - Website is fully written using Django
    - This website uses Django's authentication system, and the built in User model 
    - Some of the URLs (login, logout, register, change password) are part of Django's  django.contrib.auth.urls
    - Some of the forms are part of the Django's (UserCreationForm, UserChangeForm)  - django.contrib.auth.forms
    - Some of the views are class-based, while others are function-based  

