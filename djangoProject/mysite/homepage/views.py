from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import sqlite3
from.models import ImgTable
from .forms import PostForm
# Create your views here.
# def second(response):
#     return render(response, 'homepage/Second.html', {'name': 'I dont know'})

def index(response):
    return render(response, 'homepage/index.html')

def import_page(request):
    imp_image = PostForm(request.POST or None, request.FILES or None)
    if request.FILES:
        message = 'Image has been saved successfuly!'
        form_bgcolor = "background: rgba(0, 255, 0, 0.2);"
    else:
        message = 'Select an image and press Get Started'
        form_bgcolor = "background: rgba(255, 255, 255, 0.2);"
    if imp_image.is_valid():
        imp_image.save()
    context = {
        'imp_image': imp_image,
        'message': message,
        'form_bgcolor': form_bgcolor,
    }
    return render(request, "homepage/import.html", context)

# def import_img(request):
#     database = ImgTable.objects.last()
#     image_link = database.image
#
#     imp_image = PostForm(request.POST or None, request.FILES or None)
#     if imp_image.is_valid():
#         imp_image.save()
#     context = {
#         'imp_image': imp_image,
#         'image_link': image_link,
#              }
#     return render(request, "homepage/Second.html", context)
