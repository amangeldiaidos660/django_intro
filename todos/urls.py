from django.urls import path
from .views import add_todo, delete_todo, todo_list, todo_detail

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('<int:id>/', todo_detail, name='todo_detail'),
    path('add/', add_todo, name='add_todo'),
    path('<int:id>/delete/', delete_todo, name='delete_todo'),
]
