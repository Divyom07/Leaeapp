from django.urls import include
from django.conf.urls.static import static
from django import views
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('', views.user_view, name = 'userlogin'),
    path('manager/', views.manager_view, name ='Adminview'),
    path('profile/<str:username>/', views.profile_view, name ='profile'),
    path('createuser/', views.create_user_view, name='create user'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

