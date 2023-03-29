"""
sample tests
"""
from django.test import SimpleTestCase
from app import calc
from rest_framework.test import APIClient



class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10,15)

        self.assertEqual(res,-5)


# class TestViews(SimpleTestCase):
#     def test_get_greetings(self):
#         client = APIClient()
#         res = client.get('/greetings/')

#         self.assertEqual(res.status_code,200)
#         self.assertEqual(
#             res.data,
#             ["Hello!", "Bonjour!", "Hola!"]
#             )