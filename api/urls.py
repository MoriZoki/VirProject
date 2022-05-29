from django.urls import path
from .views import TodoList
app_name = "api"
urlpatterns = [
    path('todo', TodoList.as_view(), name="ist"),
]
