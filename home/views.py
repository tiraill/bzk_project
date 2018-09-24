from django.shortcuts import render
from .forms import MySignupForm, MyLoginForm
from django.contrib import messages
from django.shortcuts import redirect


def index_page(request):
    if request.method == 'POST':
        signup_form = MySignupForm(request.POST)
        login_form = MyLoginForm(request.POST)
        if login_form.is_valid():
            messages.success(request, ('Вы вошли!'))
            return render(request, 'index.html')
        else:
            messages.success(request, ('ошибка входа!'))
            return render(request, 'index_signup.html', {'signup_form': signup_form, 'login_form': login_form})
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, ('Ваш зарегались!'))
            return redirect('profile')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
            return render(request, 'index_signup.html', {'signup_form': signup_form})
    else:
        signup_form = MySignupForm()
        login_form = MyLoginForm()
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return render(request, 'index_signup.html', {'signup_form': signup_form, 'login_form': login_form})
