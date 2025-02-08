from django.urls import path
from .views import students_list, student_detail

urlpatterns = [
    path('', students_list, name='students_list'),
    path('<int:id>/', student_detail, name='student_detail'),
]
 