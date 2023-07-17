from unicodedata import category
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Profile, User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('users-home')
        self.register_url = reverse('users-register')
        self.settings_url = reverse('users-profile')

    #Unit Test LR1: Test that home page returns a list of articles from newsAPI
    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200) #Tests the response code is 200
        self.assertTemplateUsed(response, 'users/home.html') #tests the home url response is mapped to the correct HTML
     

    def test_register_view(self):
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


    def test_settings_view(self):
        response = self.client.post(self.settings_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')


