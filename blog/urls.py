from django.urls import path
from . import views

urlpatterns = [
    path('', views.MeetupList.as_view(), name='blog-home'),
    path('meetups/new/', views.CreateMeetup.as_view(), name='meetup-create'),
    path('meetups/<slug:slug>/', views.MeetupDetail.as_view(), name='meetup_detail'),
    path('meetups/<slug:slug>/update', views.UpdateMeetup.as_view(), name='meetup-update'),
    path('meetups/<slug:slug>/delete', views.DeleteMeetup.as_view(), name='meetup-delete'),
    path('library/', views.BookList.as_view(), name='book-list'),
    path('books/new/', views.CreateBook.as_view(), name='book-create'),
    path('books/<int:pk>/update', views.UpdateBook.as_view(), name='book-update'),
    path('books/<int:pk>/delete', views.DeleteBook.as_view(), name='book-delete'),
]
