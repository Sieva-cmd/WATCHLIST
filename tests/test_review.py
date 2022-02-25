import unittest

from app.models import Review

class TestReview(unittest.TestCase):
    
    def setUp(self):
        
        self.new_review =Review(1234,"Fantastic Movie","https://image.tmdb.org/t/p/w500/","I would recomend this movie to children")
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))     