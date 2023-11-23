from django.test import TestCase, Client
from django.urls import reverse
from degree_checklist.models import *
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.CollegeApi_url = reverse('CollegeApi')
    
    def test_CollegeApi_GET(self):
        response = self.client.get(self.CollegeApi_url)

        self.assertEquals(response.status_code, 200)

    def test_CollegeApi_POST(self):
        response = self.client.post(self.CollegeApi_url, {
            "CollegeID": "88",
            "College": "Testing CollegeAPI POST"
        })

        self.assertEquals(response.status_code, 200)

    def test_CollegeApi_POST_no_data(self):
        response = self.client.post(self.CollegeApi_url)

        self.assertEquals(response.status_code, 200)