from django.urls import path
from . import views

urlpatterns = [
    path('', views.MeetupList.as_view(), name='blog-home'),
    path('meetups/new/', views.CreateMeetup.as_view(), name='meetup-create'),
    path('meetups/<int:pk>/', views.MeetupDetail.as_view(), name='meetup_detail'),
    path('meetups/<int:pk>/update', views.UpdateMeetup.as_view(), name='meetup-update'),
    path('meetups/<int:pk>/delete', views.DeleteMeetup.as_view(), name='meetup-delete'),
    path('library/', views.BookList.as_view(), name='book-list'),
    path('books/new/', views.CreateBook.as_view(), name='book-create'),
    path('books/<int:pk>/update', views.UpdateBook.as_view(), name='book-update'),
    path('books/<int:pk>/delete', views.DeleteBook.as_view(), name='book-delete'),
    path('comments/<int:pk>/delete', views.DeleteComment.as_view(), name='comment-delete'),
    path('about/', views.about, name='blog-about'),
]
