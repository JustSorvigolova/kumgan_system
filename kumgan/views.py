from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm, BookingForm, BookingUpdateForm
from .models import Booking, Schedule, Services
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DeleteView, ListView, DetailView, UpdateView


def index(request):
    if request.user.is_superuser:  # Владелец
        return redirect('admin/')
    else:
        return render(request, 'kumgan/index.html')


def Check(request):
    try:
        da = Booking.objects.filter(title_service__title_service_booking__user=request.user.id)
        data = Booking.objects.filter(title_service__title_service_booking__user=request.user.id).last()
        context = {
            'data': data,
            'da': da
        }
        return render(request, 'kumgan/check.html', context)
    except ObjectDoesNotExist:
        messages.warning(request, "Ошибка")
        return redirect("/")


def list_client_booking_history(request):
    data = Booking.objects.filter(user=request.user)
    context = {
        'data': data
    }
    return render(request, 'kumgan/list_clinet_history.html', context)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = '/home'
    template_name = 'kumgan/delete_booking.html'


def home(request):
    if request.user.is_superuser:  # Владелец
        return redirect('admin/')
    elif request.user.is_staff or request.user.has_perm('kumgan.add_booking')\
            or request.user.is_authenticated:
        return render(request, 'kumgan/home.html')
    else:
        return render(request, 'kumgan/index.html')


def Booking_create(request):
    error = ''
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = False
            booking.save()
            print('success booking')
            return redirect('kumgan:check')
        else:
            messages.error(request, "Error in form")
    form = BookingForm()
    data = {
        'forms': form,
        'error': error,
    }
    return render(request, 'kumgan/booking.html', data)


class BookingView(ListView):
    model = Booking
    template_name = 'kumgan/booking_view.html'


class BookingUpdate(UpdateView):
    model = Booking
    template_name = 'kumgan/booking_update.html'
    form_class = BookingUpdateForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User saved")
            return redirect("kumgan:signin")
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
