# directory_app/views.py
from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm

def index(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'directory_app/index.html', {'categories': categories, 'pages': pages})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'directory_app/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'directory_app/add_page.html', {'form': form})

