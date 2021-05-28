from django.urls import path
from app import views

app_name="app"
urlpatterns=[
    path('',views.index,name='index'),
    path('/agriculture',views.pic,name='pic'),
    path('/details',views.details,name='details'),
]