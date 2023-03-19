from app2.views import *
from django.urls import path
app_name='python'

urlpatterns=[
    path('noori/',noori,name='noori'),
    path('baba/',baba,name='baba'),
]