# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('notes/', views.get_notes_list, name='notes'),
    path('notes/<str:pk>/', views.get_note_detail, name='note'),
    path('notes/create/', views.create_note, name='create-note'),
    path('notes/update/<str:pk>/', views.update_note, name='update-note'),
    path('notes/delete/<str:pk>/', views.delete_note, name='delete-note'),
]
