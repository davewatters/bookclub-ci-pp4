from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meetup, Comments


class MeetupList(generic.ListView):
    model = Meetup


class MeetupDetail(View):

    def get(self, request, slug, *args, **kwargs):
        meetup = Meetup.objects.get(slug=slug)
        comments = Comments.objects.filter(meetup=meetup.id).order_by('created_on')
        return render (
            request,
            'blog/meetup_detail.html',
            {
                'meetup': meetup,
                'comments': comments,
            },
        )
