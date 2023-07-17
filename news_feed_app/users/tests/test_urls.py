from urllib.parse import urlparse
from django.test import TestCase
from django.urls import reverse, resolve
from users.views import home, RegisterView, CustomLoginView, profile


  
class TestUrls(TestCase):
#Test home URL
    def test_home_url_is_resolve(self):
        url = reverse('users-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)


#Test registration URL
    def test_user_registration(self):
        url = reverse('users-register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterView)



#Test settings URL
    def test_user_settings(self):
        url = reverse('users-profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)