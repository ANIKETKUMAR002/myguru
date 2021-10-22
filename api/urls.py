from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [

    path('',views.api_view,name='home'),
    path('index.html',views.api_view,name='home'),
    path('signup.html',views.api_view,name='signup'),
    path('login.html',views.api_view,name='login'),
    path('guru-expert-videos.html',views.api_view,name='guru-expert-videos'),
    path('exam-list.html',views.api_view,name='exam-list'),
    path('innerpage.html',views.api_view,name='innerpage'),
    path('happiness-well-being.html',views.api_view,name='happiness-well-being'),

]