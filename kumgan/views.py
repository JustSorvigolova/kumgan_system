from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm
from .models import Booking, Schedule
from django.views.generic.edit import CreateView


def index(request):
    if request.user.is_superuser:  # Владелец
        return redirect('admin/')
    elif request.user.is_staff:  # Администратор
        return render(request, 'kumgan/admin.html')
    elif request.user.has_perm('kumgan.view_booking'):  # Сотрудник
        print('Сотрудник')
        return render(request, 'kumgan/staff.html')
    elif request.user.is_authenticated:  # Клиент
        return redirect('kumgan:home')
    else:
        return render(request, 'kumgan/index.html')


def check(request):
    return render(request, 'kumgan/check.html')


class BookingCreateView(CreateView):
    model = Booking
    fields = ['name']


def home(request):
    if request.user.is_superuser:  # Владелец
        return redirect('admin/')
    elif request.user.is_staff:  # Администратор
        return render(request, 'kumgan/admin.html')
    elif request.user.has_perm('kumgan.view_booking'):  # Сотрудник
        print('Сотрудник')
        return render(request, 'kumgan/staff.html')
    elif request.user.is_authenticated:  # Клиент
        data = Schedule.objects.all()
        return render(request, 'kumgan/home.html', {'data': data})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User saved")
            return redirect("kumgan/signup.html")
        else:
            messages.error(request, "Error in form")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "kumgan/signup.html", context)


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        username = form["username"].value()
        password = form["password"].value()
        print(password)
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            print("Successfully logged in")
            if request.user.is_superuser:  # Владелец
                return redirect('kumgan:index')
            return redirect('kumgan:home')
        else:
            print("Invalid Username or Password")
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    context = {"form": form}
    return render(request, "kumgan/signin.html", context)


def signout(request):
    logout(request)
    return redirect("kumgan:signin")
