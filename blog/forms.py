from django import forms
from .models import Comments, Meetup


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)


class MeetupForm(forms.ModelForm):

    class Meta:
        model = Meetup
        fields = '__all__'
