from django.shortcuts import render

from bookclub.settings import DEBUG


def home(request):
    testVar = DEBUG
    return render(request, 'blog/home.html', {'disp_text': testVar})