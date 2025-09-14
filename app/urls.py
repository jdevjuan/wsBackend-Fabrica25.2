from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # api :p
    path('api/tasks/', views.task_list, name='task_list'),
    path('api/tasks/create/', views.task_create, name='task_create'),
    path('api/tasks/update/<int:pk>/', views.task_update, name='task_update'),
    path('api/tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
]
