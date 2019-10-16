from django.urls import path
from . import views

urlpatterns = [
   
    path('login',views.login,name='login'),
    path('',views.index),
    path('logout',views.logout,name='logout'),
    path('createticket',views.createticket),
    path('mytickets',views.mytickets),
    path('assetlisting',views.assetlisting),
    
]