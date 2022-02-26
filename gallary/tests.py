from django.test import TestCase
from .models import Category, Photo, Location

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.travel= Category(name = 'travel')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))    