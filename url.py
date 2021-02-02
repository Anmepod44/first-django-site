from django.urls import path,re_path
from catalog.views import *
from . import views

urlpatterns=[
    path('date/',currentdate),
    path('all/',getall),
    re_path(r'^date/plus(\d{1,2})hours/$',hoursahead),
    re_path(r'^name/([A-Za-z]+)',getname)
]