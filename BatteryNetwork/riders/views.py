from django.shortcuts import render


# Create your views here.
def rider_list(request):
    return render(request, 'rider_list.html')