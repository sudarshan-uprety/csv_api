# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.data_upload, name='uploadFile'),
    path('display/', views.display_items, name='display'),
]
