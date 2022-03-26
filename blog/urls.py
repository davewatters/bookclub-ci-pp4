from django.urls import path
from . import views

urlpatterns = [
    path('', views.MeetupList.as_view(), name='blog-home'),
    # path('', views.home, name='blog-home'),
]