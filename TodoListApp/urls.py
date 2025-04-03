from django.urls import path
from .views import task_list, task_update

urlpatterns = [
    path("todos/", task_list, name="task-list"),
    path("todos/<int:pk>/", task_update, name="task-update"),
]