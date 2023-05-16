from django.contrib import admin
from .models import NovelModel, ChapterModel, Genre

# Register your models here.
admin.site.register([NovelModel, ChapterModel, Genre])