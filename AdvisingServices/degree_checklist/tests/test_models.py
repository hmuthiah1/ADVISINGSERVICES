from django.test import TestCase
from degree_checklist.models import *

class TestModels(TestCase):
    def setUp(self):
        self.College1 = College.objects.create(
            CollegeID = 21,
            College = 'College21'
        )

    def test_college_model(self):
        self.assertEquals(self.College1.total_college, 1)
