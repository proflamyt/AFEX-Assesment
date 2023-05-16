from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NovelDocument
from .models import ChapterModel
from rest_framework import serializers



class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterModel
        fields = ['date_uploaded', 'title']
    
        

class NovelDocumentSerializer(DocumentSerializer):

    chapters = ChapterSerializer(many=True)

    class Meta:
        document = NovelDocument

        fields = (
            'title',
            'overview',
            'genre',
            'authors',
            'chapters'
            
        )