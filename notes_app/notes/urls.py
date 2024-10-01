# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_list, name='notes'),
    path('notes/<str:pk>/', views.note_detail, name='note')
]
