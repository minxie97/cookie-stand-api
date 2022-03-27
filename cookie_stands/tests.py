from asyncio.windows_events import NULL
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand

class CookieStandsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = CookieStand.objects.create(location='test', owner=testuser1, description='test cookie stand', hourly_sales='null', minimum_customers_per_hour='1', maximum_customers_per_hour='1', average_cookies_per_sale='1')
        test_thing.save()

    def test_things_model(self):
        cookie_stand = CookieStand.objects.get(id=1)
        actual_owner = str(cookie_stand.owner)
        actual_location = str(cookie_stand.location)
        actual_description = str(cookie_stand.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_location, 'test')
        self.assertEqual(actual_description,'test cookie stand')
