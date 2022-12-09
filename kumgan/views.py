from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm, BookingForm, BookingUpdateForm, BoxUpdateForm, ServicesUpdateForm, \
    ScheduleUpdateCreateForm, CategoryUpdateCreateForm
from .models import Booking, Schedule, Services, Box, Category_Transport
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DeleteView, ListView, DetailView, UpdateView, CreateView


def index(request):
    if request.user.is_superuser:  # Владелец
        return redirect('admin/')
    else:
        return render(request, 'kumgan/index.html')


def Check(request):
    try:
        da = Booking.objects.filter(user=request.user)
        data = Booking.objects.filter(user=request.user.id).last()
        context = {
            'data': data,
            'da': da
        }
        print(da)
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


class PriceCreateView(CreateView):
    model = Services
    template_name = 'kumgan/price_create.html'
    fields = ['title_service', 'price_service', 'category_transport']


class PriceListView(ListView):
    model = Services
    template_name = 'kumgan/price_list.html'


class PriceDeleteView(DeleteView):
    model = Services
    template_name = 'kumgan/price_delete.html'
    success_url = '/price_list'


class PriceUpdateView(UpdateView):
    model = Services
    template_name = 'kumgan/price_update.html'
    form_class = ServicesUpdateForm


class BoxCreate(CreateView):
    model = Box
    template_name = 'kumgan/box_create.html'
    fields = ['number_of_box']


class BoxListView(ListView):
    model = Box
    template_name = 'kumgan/box_list.html'


class BoxUpdateView(UpdateView):
    model = Box
    template_name = 'kumgan/box_update.html'
    form_class = BoxUpdateForm


class BoxDeleteView(DeleteView):
    model = Box
    template_name = 'kumgan/box_delete.html'
    success_url = '/box_list'


class CategoryCreate(CreateView):
    model = Category_Transport
    template_name = 'kumgan/category_create.html'
    fields = ['type_of_car']


class CategoryListView(ListView):
    model = Category_Transport
    template_name = 'kumgan/category_list.html'


class CategoryUpdateView(UpdateView):
    model = Category_Transport
    template_name = 'kumgan/category_update.html'
    form_class = CategoryUpdateCreateForm


class CategoryDeleteView(DeleteView):
    model = Category_Transport
    template_name = 'kumgan/box_delete.html'
    success_url = '/category_list'


class BookingUpdate(UpdateView):
    model = Booking
    template_name = 'kumgan/booking_update.html'
    form_class = BookingUpdateForm


class ScheduleCreate(CreateView):
    model = Schedule
    template_name = 'kumgan/schedule_create.html'
    form_class = ScheduleUpdateCreateForm


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'kumgan/schedule_list.html'


class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = 'kumgan/schedule_update.html'
    form_class = ScheduleUpdateCreateForm


class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'kumgan/box_delete.html'
    success_url = '/schedule_list'


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
