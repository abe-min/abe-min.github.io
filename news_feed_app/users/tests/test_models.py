from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User

class TestModel(TestCase):
    def test_should_create_user(self):
        user=User.objects.create_user(username='username')
        user.set_password('password12!')
        user.save()
        self.assertEqual(str(user),'username')
