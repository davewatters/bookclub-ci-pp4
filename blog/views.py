from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class CreateMeetup(LoginRequiredMixin, generic.CreateView):
    '''
    Allows user to add a new Meetup record
    '''
    model = Meetup
    fields = '__all__'


class UpdateMeetup(LoginRequiredMixin, generic.UpdateView):
    '''
    Allows user to modify an exsiting Meetup record
    '''
    model = Meetup
    fields = '__all__'


class DeleteMeetup(LoginRequiredMixin, generic.DeleteView):
    '''
    Allows user to delete a Meetup record
    '''
    model = Meetup
    success_url = '/'

##
# CRUD Functions for Books 
#
class CreateBook(LoginRequiredMixin, generic.CreateView):
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


class UpdateBook(LoginRequiredMixin, generic.UpdateView):
    '''
    Allow user to modify an exsiting Book record
    '''
    model = Book
    fields = '__all__'


class DeleteBook(LoginRequiredMixin, generic.DeleteView):
    '''
    Allow user to delete a Book record
    '''
    model = Book
    success_url = '/library/'


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Allow user to delete comment. Remain on meetup_detail page.
    User can delete comment only if they created it.
    '''
    model = Comments    
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False

    def get_success_url(self):
        # On successful delete stay on same meetup page
        meetup = self.object.meetup
        return reverse_lazy('meetup_detail', kwargs={'slug': meetup.slug})
