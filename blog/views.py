from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Meetup


class MeetupList(generic.ListView):
    model = Meetup


class MeetupDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Meetup.objects.all()
        meetup = get_object_or_404(queryset, slug=slug)

        return render (
            request,
            'blog/meetup_detail.html',
            {
                'meetup': meetup,
            },
        )
