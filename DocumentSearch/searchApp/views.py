import abc
import logging

from elasticsearch_dsl import Q
from elasticsearch.exceptions import ConnectionError

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView


from searchapp.utils.handlers import ConnectionErrorException

from .documents import NovelDocument
from .serializers import NovelDocumentSerializer


logger = logging.getLogger(__name__)


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request):
        try:
            query = request.GET.get('q', '')
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
         
            return self.get_paginated_response(serializer.data)
        
        except ConnectionError as e:
            logger.error(f"connection Error: {str(e)}")
            raise ConnectionErrorException('ElasticDatabase is Unvailable')






class NovelDocumentView(PaginatedElasticSearchAPIView):
    serializer_class = NovelDocumentSerializer
    document_class = NovelDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query, 
                type="best_fields", tie_breaker=0.3,
                fields=[   
                    'overview',
                    'authors.username'
                    'title',
                ], fuzziness='auto')


