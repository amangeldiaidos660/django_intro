from django.shortcuts import redirect, render, get_object_or_404
from .models import Todos
from .forms import TodoForm

def todo_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todos, pk=id)
    return render(request, 'todo_detail.html', {'todo': todo})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todos, id=id)
    todo.delete()
    return redirect('todo_list')
