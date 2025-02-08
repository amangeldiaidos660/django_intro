from django.shortcuts import render, get_object_or_404
from .models import Student

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/student_detail.html', {'student': student})
