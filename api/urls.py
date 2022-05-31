from django.urls import path
from .views import TodoDestroy, TodoList, TodoEdit, TodoUpdate
app_name = "api"
urlpatterns = [
    path('todo', TodoList.as_view(), name="ist"),
    path('todo/<int:pk>', TodoEdit.as_view(), name="todo-edit"),
    path('todo/update/<int:pk>', TodoUpdate.as_view(), name="todo-update"),
    path('todo/delete/<int:pk>', TodoDestroy.as_view(), name="todo-delete"),
]
