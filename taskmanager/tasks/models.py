from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100,verbose_name='Titulo')
    description=models.TextField(blank=True,verbose_name='Descripcion')
    completed=models.BooleanField(default=False,verbose_name='Completado')
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Tarea'
        verbose_name_plural='Tareas'
    def __str__(self):
        return self.title