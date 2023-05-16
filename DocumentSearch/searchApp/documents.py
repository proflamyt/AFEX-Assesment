from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document, fields, registries
from .models import NovelModel


@registries.registry.register_document
class NovelDocument(Document):
    chapters = fields.NestedField(properties={
        'title': fields.TextField(),
        'pk': fields.IntegerField(),
    })
    genres = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    
    })
    authors = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
    
    })

    class Index:
        name = 'novels'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = NovelModel
        fields = [
            'title',
            'overview',

        ]