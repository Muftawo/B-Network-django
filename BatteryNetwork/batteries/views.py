from django.shortcuts import render


# Create your views here.
def battery_list(request):
    return render(request, 'batteries/battery_list.html')