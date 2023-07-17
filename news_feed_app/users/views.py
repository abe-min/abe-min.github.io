from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
import requests
from newsapi import NewsApiClient
from .forms import RegisterForm, LoginForm, UpdateProfileForm
from rest_framework import viewsets
from .serializers import profileSerializer
from .models import Profile
from .forms import UpdateProfileForm
import requests, json

API_KEY1 = '8512df4f49b74b3bbbf5745f9d59d5ba' #Abe API key
API_KEY = 'c0b4174735c647798d1e72df1385ee5d'

def home(request):
    default_category = 'general'
    category = request.GET.get('category')
    searchkeyword = request.GET.get('searchkeyword')
    page_num = request.GET.get('page_num')
    language = request.GET.get('language')
    user_selection =[]

    #for getattr(UpdateProfileForm.__class__, <field_name>) in UpdateProfileForm:
            #if field is True:
                #user_selection.append(field)

    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}&pageSize=5&page={page_num}&language=en'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    elif searchkeyword:
        url = f'https://newsapi.org/v2/everything?q={searchkeyword}&apiKey={API_KEY}&pageSize=5&page={page_num}&language=en'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={default_category}&apiKey={API_KEY}&pageSize=5&page={page_num}&language=en'
        response = requests.get(url)
        #x = response.json()
        #z = json.loads(x)
        #z.update(x)
        #data = json.dumps(z)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'users/home.html', context)









#user_key = ['Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology']
##news api view
#def home(request):
#    newsapi = NewsApiClient(api_key ='8512df4f49b74b3bbbf5745f9d59d5ba')
#    meh = []
#    #top = []
#    
#    top = newsapi.get_top_headlines(category='general')
#    l = top['articles']
#    desc =[]
#    news =[]
#    img =[]
#    cat =[]
#  
#    for i in range(len(l)):
#        f = l[i]
#        news.append(f['title'])
#        desc.append(f['description'])
#        img.append(f['urlToImage'])
#        #cat.append(f['category'])
#    mylist = zip(news, desc, img)
#    #mylist = zip(meh)
#    return render(request, 'users/home.html', context ={"mylist":mylist})
#    print (meh)




class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
  
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Remember me functionality 
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
    
            self.request.session.set_expiry(0)

      
            self.request.session.modified = True

     
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your Settings have been saved successfully')
            return redirect(to='users-profile')

    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})












#To be implemented in a later sprint

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')