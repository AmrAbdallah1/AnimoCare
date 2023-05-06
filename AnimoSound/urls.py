from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('api/', views.upload_files, name='api'),
    path('api2/', views.Get_Emotion, name='api2'),
    
]







