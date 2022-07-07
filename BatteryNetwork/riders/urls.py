
from django.urls import path
from .import views


urlpatterns = [
    path('', views.rider_list)

]
