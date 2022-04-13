from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from .models import Meetup, Comments, Book
from .forms import CommentForm, MeetupForm


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
    Accepts New & displays associated User Comments.
    '''
    def get(self, request, pk, *args, **kwargs):
        meetup = Meetup.objects.get(pk=pk)
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

    def post(self, request, pk, *args, **kwargs):
        meetup = Meetup.objects.get(pk=pk)
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


class CreateMeetup(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    '''
    Allows user to add a new Meetup record. Only a meetup organiser
    can do this (orgainser has auth_user.is_staff bool set to True).
    '''
    model = Meetup
    fields = [
        'title',
        'meetup_date',
        'book1',
        'details',
    ]

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class UpdateMeetup(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''
    Allows user to modify an exsiting Meetup record. Only a meetup organiser
    can do this (orgainser has auth_user.is_staff bool set to True).
    '''
    model = Meetup
    fields = [
        'title',
        'meetup_date',
        'book1',
        'details',
        'status',
    ]

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        # Update modified_by with the current user
        form.instance.modified_by = self.request.user
        return super().form_valid(form)


class DeleteMeetup(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Allows user to delete a Meetup record. Only a meetup organiser
    can do this (orgainser has auth_user.is_staff bool set to True).
    '''
    model = Meetup
    success_url = '/'

    def test_func(self):
        return self.request.user.is_staff


##
# CRUD Functions for Books 
#
class CreateBook(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    '''
    Allow user to add a new Book record. Only a meetup organiser
    can do this (orgainser has auth_user.is_staff bool set to True).
    '''
    model = Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_staff


class BookList(generic.ListView):
    '''
    Display list of all Books.
    '''
    model = Book
    ordering = ['title']

    def test_func(self):
        return self.request.user.is_staff


class UpdateBook(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    '''
    Allow user to modify an exsiting Book record.
    Only a meetup organiser can do this.
    '''
    model = Book
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_staff


class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Allow user to delete a Book record.
    '''
    model = Book
    success_url = '/library/'

    def test_func(self):
        return self.request.user.is_staff


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    '''
    Allow user to delete comment. Remain on meetup_detail page.
    User can delete comment only if they created it.
    '''
    model = Comments    
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

    def get_success_url(self):
        # On successful delete, stay on same meetup page
        meetup = self.object.meetup
        return reverse_lazy('meetup_detail', kwargs={'pk': meetup.pk})


##
# About Page
#
def about(request):
    return render(request, 'blog/about.html')