from django.shortcuts import render
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    username = 'Robert'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def create_project(request):

    if request.method == 'POST':
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    else:
        return render(request, 'projects/create_project.html')

def project_detail(request,id):

    project = get_object_or_404(Project,id=id)
    tasks = Task.objects.filter(project_id = id)
    return render(request,'projects/project_detail.html',{
            'project':project,
            'tasks':tasks
        })

 
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):

    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=request.POST['project'])
        return redirect('tasks')
    else:
        project = Project.objects.all()
        return render(request, 'tasks/create_task.html',{
            'projects':project
        })
    
def update_task_form(request,id):
    projects = Project.objects.all()
    task = Task.objects.get(id=id)
    return render(request,'tasks/update_task_form.html', {
        'task':task,
        'projects': projects
    })    
    
def update_task(request):

    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        description = request.POST['description']
        project = request.POST['project']

        task = Task.objects.get(id=id)
        task.title = title
        task.description = description
        task.project_id = project

        task.save()

    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    
def delete_task(request,id):
    
    instance = Task.objects.get(id=id)
    instance.delete()
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })