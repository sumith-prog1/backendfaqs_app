from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question='What is Django?',
            answer='Django is a web framework.'
        )

    def test_translation_creation(self):
        self.assertTrue(self.faq.question_hi)

    def test_api_language_param(self):
        client = APIClient()
        response = client.get(reverse('faq-list'), {'lang': 'hi'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['question'], self.faq.question_hi)