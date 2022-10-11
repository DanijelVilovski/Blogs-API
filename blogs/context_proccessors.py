from .models import Category

def navbar_context(request):
    return {'cat_menu': Category.objects.all(), }

# We made this file so all that category objects could always be available on the navbar drop menu, independent of which page we are on.
# We added 'blogs.context_proccessors.navbar_context' in templates in options in settings.py.
# In base.html, through for loop, we provided all categories:
# {% for category in cat_menu %}
#     <a class="dropdown-item" href="{% url 'category' category.name %}"> {{ category.name }} </a>
# {% endfor %}