from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm


def todo_add(request, list_id):
    todo_list = get_object_or_404(TodoList, pk=list_id)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list  
            todo.save()
            return redirect("todo_list_detail", id=list_id)
    else:
        form = TodoForm()
    return render(request, "todo_form.html", {"form": form, "todo_list": todo_list})


def todo_lists(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    
    lists = TodoList.objects.all()
    return render(request, 'todo_lists.html', {'lists': lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todos = todo_list.todos.all()
    return render(request, 'todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

def todo_list_edit(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todo_list_edit.html', {'form': form})

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todo_list.delete()
    return redirect('todo_lists')

def todo_edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_edit.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)
