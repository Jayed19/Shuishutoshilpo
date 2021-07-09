from django.urls import path,include
from . import views


urlpatterns = [
   
    path('', views.authlogin,name='login'),
    path('registration', views.registration,name='login.registration'),
    path('profile', views.profile,name='login.profile'),
    path('logout', views.userlogout,name='logout.profile'),

]
