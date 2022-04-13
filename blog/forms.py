from django import forms
from .models import Book, Comments, Meetup


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('body',)


class MeetupForm(forms.ModelForm):
    
    class Meta:
        model = Meetup
        fields = '__all__'


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
