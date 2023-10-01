from django.urls import path
from App1.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]