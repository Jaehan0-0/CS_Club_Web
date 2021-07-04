from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Mainpage.as_view()),
    path('aboutclub', views.AboutClub.as_view()),
    path('members', views.Members.as_view()),
    path('projects', views.Projects.as_view()),
]