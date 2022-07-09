from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from home_app.forms import LoginRegister, UserRegister, WorkerRegister


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_user:
                return redirect('user_home')
            elif user.is_worker:
                return redirect('worker_home')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login.html')


def user_register(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, 'user registration successful')
            return redirect('login_view')
    return render(request, 'user_temp/user_register.html', {'login_form': login_form, 'user_form': user_form})


def worker_registration(request):
    login_form = LoginRegister()
    worker_form = WorkerRegister()
    if request.method == "POST":
        login_form = LoginRegister(request.POST)
        worker_form = WorkerRegister(request.POST)
        if login_form.is_valid() and worker_form.is_valid():
            user = login_form.save(commit=False)
            user.is_worker = True
            user.save()
            w = worker_form.save(commit=False)
            w.user = user
            w.save()
            messages.info(request, 'message created successful')
            return redirect('login_view')
    return render(request, 'worker_temp/worker_register.html', {'login_form': login_form, 'worker_form': worker_form})


def log_out(request):
    logout(request)
    return redirect('/')
