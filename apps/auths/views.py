# Django
from django.shortcuts import (
    render,
    redirect,    
)
from django.contrib.auth import (
    login,
    logout,
    authenticate
)
from django.contrib.auth.hashers import (
    make_password,
)
from django import views
from django.http import (
    HttpRequest,
    HttpResponse,
)

# Local
from .forms import (
    RegistrationForm,
    LoginForm,
)
from .models import Client


class RegistrationView(views.View):
    """Registrarion view."""
    form = RegistrationForm

    def get(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        """GET."""
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_title': 'Registration Page',
                'ctx_form': self.form(),
                'ctx_link': {
                    'text': 'Already have account?',
                    'link': '/login'
                },
                'ctx_action': 'Register'
            },
            status=200
        )


    def post(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        """POST."""
        data: RegistrationForm = self.form(
            request.POST
        )
        if not data.is_valid():
            return render(
                request=request,
                template_name='index.html',
                context={
                    'ctx_title': 'Registration Page',
                    'ctx_form': self.form(),
                    'ctx_link': {
                        'text': 'Already have account?',
                        'link': '/login'
                    },
                    'ctx_action': 'Register',
                    'ctx_error': 'This login already used'
                },
                status=200
            )
        user_login = data.cleaned_data.get('login')
        password = data.cleaned_data.get('password')
        password2 = data.cleaned_data.get('password2')
        if password != password2:
            return render(
                request=request,
                template_name='index.html',
                context={
                    'ctx_title': 'Registration Page',
                    'ctx_form': self.form(),
                    'ctx_link': {
                        'text': 'Already have account?',
                        'link': '/login'
                    },
                    'ctx_action': 'Register',
                    'ctx_error': 'Passwords not the same!'
                },
                status=200
            )
        Client.objects.create_user(
            login=user_login,
            password=password
        )
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_title': 'Registration Page',
                'ctx_form': self.form(),
                'ctx_link': {
                    'text': 'Already have account?',
                    'link': '/login'
                },
                'ctx_action': 'Register',
                'ctx_error': 'Success!'
            },
            status=200
        )


class LoginView(views.View):
    """Login view."""
    form = LoginForm

    def get(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        """GET."""
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_title': 'Login Page',
                'ctx_form': self.form(),
                'ctx_link': {
                    'text': 'Have not account?',
                    'link': '/reg'
                },
                'ctx_action': 'Login'
            },
            status=200
        )
    

    def post(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        """POST."""
        data: LoginForm = self.form(
            request.POST
        )
        user_login = data.data.get('login')
        password = data.data.get('password')
        user = authenticate(
            request=request,
            username=user_login,
            password=password
        )
        if not user:
            return render(
                request=request,
                template_name='index.html',
                context={
                    'ctx_title': 'Login Page',
                    'ctx_form': self.form(),
                    'ctx_link': {
                        'text': 'Have not account?',
                        'link': '/reg'
                    },
                    'ctx_action': 'Login',
                    'ctx_error': 'Invalid data'
                },
                status=200
            )
        login(
            request=request,
            user=user
        )
        return redirect('/')


class LogoutView(views.View):
    """Logout view."""
    def get(self, request: HttpRequest,
            *args: tuple, **kwargs: dict) -> HttpResponse:
        """GET."""
        logout(request=request)
        return redirect('/login')