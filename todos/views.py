from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

# ✅ Барлық Todo тізімін алу (GET todos/)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# ✅ Белгілі бір Todo-ны көру (GET todos/:id)
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# ✅ Жаңа Todo жасау (POST todos/new/)
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Барлық Todos бетіне қайта бағыттау
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# ✅ Todo-ны өңдеу (UPDATE todos/:id/edit)
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})

# ✅ Todo-ны өшіру (DELETE todos/:id/delete)
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')  # Барлық Todos бетіне қайта бағыттау

# ✅ API арқылы JSON форматында барлық Todos тізімін қайтару
def api_todo_list(request):
    todos = Todo.objects.all().values('id', 'title', 'description', 'due_date', 'status')
    return JsonResponse(list(todos), safe=False)

# ✅ API арқылы JSON форматында бір Todo қайтару
def api_todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return JsonResponse({
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'due_date': str(todo.due_date),
        'status': todo.status
    })
