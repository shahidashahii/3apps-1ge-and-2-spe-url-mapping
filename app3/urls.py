from app3.views  import *
from django.urls import path
app_name='sql'
urlpatterns=[
    path('abhi/',abhi,name='abhi'),
    path('rizzu/',rizzu,name='rizzu'),
]