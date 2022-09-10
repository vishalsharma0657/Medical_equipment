from django.contrib import admin
from django.urls import path , include
from medicall import views

urlpatterns = [
    # path('', views.index , name='home'),
    path('user', views.user , name='user'),
    path('user/<str:pk>', views.user1 , name='user1'),
    path('addUser', views.addUser , name='addUser'),
    path('auth',views.auth,name='auth')

]