from django.shortcuts import render
from django.views import generic
from .models import Meetup

from bookclub.settings import DEBUG


def home(request):
    testVar = DEBUG
    return render(request, 'blog/home.html', {'disp_text': testVar})


class MeetupList(generic.ListView):
    model = Meetup