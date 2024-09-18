

from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, AddNumberView

app_name = 'tasks_api'

urlpatterns = [
    path('tasks/' , TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('add/', AddNumberView.as_view(), name='add-numbers'),  # Add this route for adding numbers
]