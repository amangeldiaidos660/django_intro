from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TodoForm
from .models import Todo

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todos')
    else:
        form = RegisterForm()
    return render(request, 'reg/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todos')
    else:
        form = AuthenticationForm()
    return render(request, 'reg/login.html', {'form': form})

@login_required
def todos_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'reg/todos.html', {'todos': todos})

@login_required
def todo_detail_view(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'reg/todo_detail.html', {'todo': todo})

@login_required
def todo_create_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos')
    else:
        form = TodoForm()
    return render(request, 'reg/todo_form.html', {'form': form})

@login_required
def todo_delete_view(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todos')
