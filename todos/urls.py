from django.urls import path
from .views import todo_list, todo_detail, todo_create, todo_update, todo_delete, api_todo_list, api_todo_detail

urlpatterns = [
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todos/new/', todo_create, name='todo_create'),
    path('todos/<int:todo_id>/edit/', todo_update, name='todo_update'),
    path('todos/<int:todo_id>/delete/', todo_delete, name='todo_delete'),

    # API маршруттары
    path('api/todos/', api_todo_list, name='api_todo_list'),
    path('api/todos/<int:todo_id>/', api_todo_detail, name='api_todo_detail'),
]
