from django.urls import path
from .views import task_list, task_update
from .views import SecureHelloView

urlpatterns = [
    path('secure-hello/', SecureHelloView.as_view()),
    path("todos/", task_list, name="task-list"),
    path("todos/<int:pk>/", task_update, name="task-update"),
]