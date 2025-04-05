from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('todos/', views.todos_view, name='todos'),
    path('todos/create/', views.todo_create_view, name='todo_create'),
    path('todos/<int:id>/', views.todo_detail_view, name='todo_detail'),
    path('todos/<int:id>/delete/', views.todo_delete_view, name='todo_delete'),
]
