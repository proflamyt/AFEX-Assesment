from django.urls import path
from .views import NovelDocumentView


urlpatterns = [

    path('search', NovelDocumentView.as_view(), name='novel-search')
]
