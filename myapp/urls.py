from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/',views.about, name = 'about'),
    path('projects/', views.projects, name = 'projects'),
    path('create_project/', views.create_project, name = 'create_project'),
    path('project_detail/<int:id>', views.project_detail, name = 'project_detail'),
    path('tasks/', views.tasks, name = 'tasks'),
    path('create_task/',views.create_task, name = 'create_task'),
    path('delete_task/<int:id>',views.delete_task, name='delete_task'),
    path('update_task_form/<int:id>',views.update_task_form, name='update_task_form'),
    path('update_task',views.update_task, name='update_task')
]