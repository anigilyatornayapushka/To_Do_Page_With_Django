# Django
from django.shortcuts import (
    render,
    redirect,
)
from django.db.models.query import QuerySet
from django.http import (
    HttpResponse,
    HttpRequest,
)
from django import views

# Local
from .models import Tasks
from .forms import TasksForm


class TasksView(views.View):
    """Main tasks view."""
    form = TasksForm

    def get(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        tasks: QuerySet[Tasks] = Tasks.objects.filter(publisher=request.user)
        return render(
            request=request,
            template_name='main.html',
            context={
                "ctx_title": "Task Page",
                "ctx_tasks": tasks,
                "ctx_form": self.form()
            }
        )


    def post(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        data: TasksForm = self.form(
            request.POST
        )
        Tasks.objects.create(
            progress=data.data.get('progress'),
            publisher=request.user,
            title=data.data.get('title'),
            description=data.data.get('description'),
        )
        return redirect('/')


class DeleteTasksView(views.View):
    """View to delete tasks."""
    def get(self,
            request: HttpRequest,
            id: str, *args: tuple,
            **kwargs: dict) -> HttpResponse:
        task = Tasks.objects.get(id=id)
        task.delete()
        return redirect('/')


class UpdateTasksView(views.View):
    """View to update tasks status."""
    def get(self,
            request: HttpRequest,
            id: str, *args: tuple,
            **kwargs: dict) -> HttpResponse:
        task = Tasks.objects.get(id=id)
        task.progress = (task.progress + 1)%2
        task.save(
            update_fields=(
                'progress',
            )
        )
        return redirect('/')


class TasksDescriptionView(views.View):
    """View to update tasks status."""
    def get(self,
            request: HttpRequest,
            id: str, *args: tuple,
            **kwargs: dict) -> HttpResponse:
        task = Tasks.objects.get(id=id)
        return render(
            request=request,
            template_name='description.html',
            context={
                'ctx_title': task.title,
                'ctx_description': task.description,
            }
        )
    