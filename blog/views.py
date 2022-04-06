from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Meetup, Comments, Book
from .forms import CommentForm


class MeetupList(generic.ListView):
    model = Meetup


class BookList(generic.ListView):
    model = Book
    ordering = ['title']


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
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        meetup = Meetup.objects.get(slug=slug)
        comments = Comments.objects.filter(meetup=meetup.id).order_by('created_on')
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            new_comment = comment_form.save(commit=False)
            new_comment.meetup = meetup
            new_comment.save()
        else:
            comment_form = CommentForm()

        return render (
            request,
            'blog/meetup_detail.html',
            {
                'meetup': meetup,
                'comments': comments,
                'comment_form': comment_form,
            },
        )


class CreateMeetup(generic.CreateView):
    model = Meetup
    fields = '__all__'


class UpdateMeetup(generic.UpdateView):
    model = Meetup
    fields = '__all__'


class DeleteMeetup(generic.DeleteView):
    model = Meetup
    success_url = '/'


