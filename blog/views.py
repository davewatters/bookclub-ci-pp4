from django.shortcuts import render
from django.views import generic
from .models import Meetup

from bookclub.settings import DEBUG


class MeetupList(generic.ListView):
    model = Meetup