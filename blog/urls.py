from django.urls import path
from . import views

urlpatterns = [
    path('', views.MeetupList.as_view(), name='blog-home'),
    path('meetups/<slug:slug>/', views.MeetupDetail.as_view(), name='meetup_detail'),
]