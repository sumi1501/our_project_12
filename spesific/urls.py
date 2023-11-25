from  spesific.views import *
from django.urls import path
app_name='mathss'
urlpatterns=[
    path('maths/',maths,name='maths'),
]