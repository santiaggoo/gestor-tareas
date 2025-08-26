from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('task_list')
        else:
            messages.error(request,'Error al Registrarse')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})      

def login_view(request):
    if request.method== 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request,'Usuario o Contraseña incorrectos')
    else:
        form=AuthenticationForm()        
    return render(request,'tasks/login.html',{
            'form':form
        })
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('task_list')
    else:
            form=TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

@login_required
def edit_task(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    if request.method== 'POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=task)
    return render(request,'tasks/edit_task.html',{
        'form':form
    })  

@login_required
def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)  
    if request.method == 'POST':
        task.delete()
        return redirect('task_list') 

    return render(request, 'tasks/delete_task.html', {'task': task})

    


        
