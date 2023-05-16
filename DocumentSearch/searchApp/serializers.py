from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NovelDocument

class NovelDocumentSerializer(DocumentSerializer):
    class Meta:
        document = NovelDocument

        fields = (
            'title',
            'overview'
        )