from django.db import models
from django.conf import settings

# Create your models here.

class NovelModel(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='books')
    readers_num = models.IntegerField(default=0)
    ratings = models.IntegerField(default=5.0)
    genre = models.ManyToManyField('Genre')
    overview = models.TextField()
    weekly_featured = models.BooleanField(default=False)
    special_featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title
    


class ChapterModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    book = models.ForeignKey(NovelModel, on_delete=models.CASCADE, related_name='chapters', null=True,)
    content = models.TextField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.book.title}:{self.title} "
    


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name