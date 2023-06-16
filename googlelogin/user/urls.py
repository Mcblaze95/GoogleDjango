from django.urls import path 
from . import views
from .views import index


urlpatterns = [
    path('', views.home1),
    path('index/', index, name='index'),
    path('logout', views.logout_view)

    
  
    
]
