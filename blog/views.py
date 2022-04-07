from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from .models import Meetup, Comments, Book
from .forms import CommentForm


##
# CRUD Functions for club Meetup details
#
class MeetupList(generic.ListView):
    '''
    Displays list of all Meetups.
    '''
    model = Meetup


class MeetupDetail(View):
    '''
    Displays details of selected Meetup.
    Accepts New & Displays associated User Comments.
    '''
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
    '''
    Allows user to add a new Meetup record
    '''
    model = Meetup
    fields = '__all__'


class UpdateMeetup(generic.UpdateView):
    '''
    Allows user to modify an exsiting Meetup record
    '''
    model = Meetup
    fields = '__all__'


class DeleteMeetup(generic.DeleteView):
    '''
    Allows user to delete a Meetup record
    '''
    model = Meetup
    success_url = '/'

##
# CRUD Functions for Books 
#
class CreateBook(generic.CreateView):
    '''
    Allow user to add a new Book record
    '''
    model = Book
    fields = '__all__'


class BookList(generic.ListView):
    '''
    Display list of all Books.
    '''
    model = Book
    ordering = ['title']


class UpdateBook(generic.UpdateView):
    '''
    Allow user to modify an exsiting Book record
    '''
    model = Book
    fields = '__all__'


class DeleteBook(generic.DeleteView):
    '''
    Allow user to delete a Book record
    '''
    model = Book
    success_url = '/library/'


class DeleteComment(generic.DeleteView):
    '''
    Allow user to delete their own comment
    '''
    model = Comments
    # print('*'*50)
    # print(model)
    # print('*'*50)
    # print(model.objects.get(slug=))
    # print('*'*50)

    # After successful comment delete I wan to stay on current page
    # Need to find a way to redirect to meetups/<slug:slug>/
    success_url = ('/')