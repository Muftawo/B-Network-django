from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("about the page")


def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')