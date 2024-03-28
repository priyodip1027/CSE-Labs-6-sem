# website_directory/urls.py
from django.contrib import admin
from django.urls import path
from directory_app.views import index, add_category, add_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_category/', add_category, name='add_category'),
    path('add_page/', add_page, name='add_page'),
]

