from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('index.html', views.home, name='index'),  # URL for index.html
    path('completed', views.completed, name='completed'),
    path('remaining', views.remaining, name='remaining'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<str:task_id>', views.delete_task, name='delete_task'),
    path('go_back_view', views.go_back_view, name='go_back_view'),
    path('detail/<str:task_id>', views.task_detail, name='task_detail'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='toggle_complete'),
    path('toggle_remaining/<str:task_id>', views.toggle_remaining, name='toggle_remaining'),
    path('toggle_home/<str:task_id>', views.toggle_home, name='toggle_home'),
    path('remove_task/<str:task_id>', views.remove_task, name='remove_task'),
]