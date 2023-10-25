from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            # 如果要在注册后立即登录用户，使用以下代码
            # login(request, user)

            return redirect('login')  # 重定向到登录页面或其他页面
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 重定向到 'home' 页面
            else:
                messages.error(request, '用户名或密码不正确')  # 添加密码错误的错误消息
        else:
            messages.error(request, '表单验证失败，请检查您的输入')  # 表单验证失败的错误消息
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def jsj_views(request):
    return render(request, 'registration/jsj.html')


@login_required
def home_view(request):
    return render(request, 'registration/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # 重定向到登录页面或其他页面


@login_required
def user_list(request):
    return render(request, 'registration/sc/secondary_page.html')

@login_required
def Guess_the_numbers(request):
    return render(request, 'registration/sc/guessnumber.html')