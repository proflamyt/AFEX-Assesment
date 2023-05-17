from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document, fields, registries
from .models import NovelModel
from elasticsearch_dsl.analysis import analyzer, token_filter

my_analyzer = analyzer(
    'my_analyzer',
    tokenizer='standard',
    filter=[
        'lowercase',
        token_filter('english_stemmer', type='stemmer', language='english')
    ]
)


        
@registries.registry.register_document
class NovelDocument(Document):
    title = fields.TextField(analyzer=my_analyzer)

    overview = fields.TextField(analyzer=my_analyzer)

    chapters = fields.NestedField(properties={
        'title': fields.TextField(),
        'pk': fields.IntegerField(),
    })
    genre = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    
    })
    authors = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(analyzer=my_analyzer),
    
    })

    class Index:
        name = 'novels'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0,
                    "index" : {
        "similarity" : {
          "default" : {
            "type" : "BM25",
            "b": 0,
            "k1": 10
          }
        }
    }
  }
                    
        

    class Django:
        model = NovelModel
        fields = [
        ]