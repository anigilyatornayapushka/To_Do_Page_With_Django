# Django
from django.contrib import admin
from django.urls import path

# Third-Party
from todo.views import (
    TasksView,
    UpdateTasksView,
    DeleteTasksView,
    TasksDescriptionView
)
from auths.views import (
    LoginView,
    LogoutView,
    RegistrationView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('reg/', RegistrationView.as_view()),

    path('', TasksView.as_view()),
    path('task/update-status/<str:id>', UpdateTasksView.as_view()),
    path('task/delete/<str:id>', DeleteTasksView.as_view()),
    path('task/description/<str:id>', TasksDescriptionView.as_view()),
]
