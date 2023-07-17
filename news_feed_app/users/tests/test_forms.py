from django.test import TestCase
from users.forms import RegisterForm, LoginForm, UpdateProfileForm


class TestForms(TestCase):

    def test_register_form(self):

        form = RegisterForm(data={
            'username': 'newuser',
            'password': 'Meh123456!',
            'password2': 'Meh123456!'
        })

        self.assertTrue(form.is_valid()) #checks that form is valid
    
    def test_register_form_no_data(self):
        form = RegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_login_form(self):
        form = LoginForm(data={
            'username': 'newuser',
            'password': 'Test123!'
        })

        self.assertTrue(form.is_valid())

    def test_settings_form(self):
        form = UpdateProfileForm(data={
        'Business': 'True',
        
        })

        self.assertTrue(form.is_valid())