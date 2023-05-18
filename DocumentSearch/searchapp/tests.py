from unittest import mock
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.core.management import call_command

from .utils.handlers import ConnectionErrorException

from .views import NovelDocumentView
from .documents import NovelDocument
from .models import NovelModel



class NovelDocumentViewTest(TestCase):

   
    def setUp(self):
        """
        populating database with test data
        """
       # call_command('populate_db')
        self.factory = RequestFactory()
        self.query = {'q': "of the"} 
        self.url = reverse('novel-search')

    def test_model_class_added(self):
        """
        Test If elasticsearch database has been populated
        """
        self.assertEqual(NovelDocument.django.model, NovelModel)


    def test_search_endpoint(self):
        """
        test the search endpoint, and check the similarity ranking
        """
        
        expected_results =  ('The Journey', 'Game of Throne')
        
        response = self.client.get(self.url, self.query)
        self.assertEqual(response.status_code, 200)
        results = response.json().get('results')
       
        
        actual_results = results[0]['title'], results[1]['title']
        self.assertEqual(actual_results, expected_results)

    
    def test_connection_error(self):
        """ Mock the Elasticsearch client to raise ConnectionError """
        
        request = self.factory.get(self.url, self.query)

 
        with mock.patch('searchapp.views.NovelDocumentView.document_class.search') as mock_search:
            mock_search.side_effect = ConnectionErrorException('Mocked ConnectionError')
            
            view = NovelDocumentView.as_view()
                    
            response = view(request)
            self.assertEqual(response.status_code, 503)
            





