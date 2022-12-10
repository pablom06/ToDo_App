
from django.urls import path
from django.views import View
from Todo_App.views import HomeView, TaskDetailView

urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('<int:task_id>', TaskDetailView.as_view(), name='task_detail'),
        ]