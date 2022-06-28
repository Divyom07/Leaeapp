from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django import views
from . import views

urlpatterns = [
    path('', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
