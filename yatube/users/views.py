# Импортируем CreateView, чтобы создать ему наследника
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy("posts:index")
    template_name = "users/signup.html"
