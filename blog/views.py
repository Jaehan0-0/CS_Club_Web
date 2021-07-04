from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

#import pyrebase
'''
config = {
    "apiKey": "AIzaSyALVobVh6u2VRXv3Ot2OVtFWD22ynz_E9M",
    "authDomain": "ssi-cs-club.firebaseapp.com",
    "databaseURL": "https://ssi-cs-club-default-rtdb.firebaseio.com",
    "projectId": "ssi-cs-club",
    "storageBucket": "ssi-cs-club.appspot.com",
    "messagingSenderId": "384774499123",
    "appId": "1:384774499123:web:4f5ea49644645acac66c46",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
'''

# Create your views here.
class Mainpage(ListView):
    model = Post
    template_name = 'blog/Mainpage.html'

class AboutClub(ListView):
    model = Post
    template_name = 'blog/AboutClub.html'

class Members(ListView):
    model = Post
    template_name = 'blog/Members.html'

class Projects(ListView):
    model = Post
    template_name = 'blog/Projects.html'