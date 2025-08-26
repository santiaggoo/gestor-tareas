from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('task_list',views.task_list,name='task_list'),
    path('create-task/',views.create_task,name='create-task'),
    path('edit-task/<int:task_id>/',views.edit_task,name='editar'),
    path('delete-task/<int:task_id>/',views.delete_task,name='eliminar'),

]
