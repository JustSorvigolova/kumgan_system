from django.urls import path
from kumgan import views

app_name = 'kumgan'

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('check/', views.Check, name='check'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('booking/', views.Booking_create, name='booking'),
    path('booking_view/', views.BookingView.as_view(), name='booking_view'),
    path('<int:pk>/booking_update', views.BookingUpdate.as_view(), name='booking_update'),
    path('box_create/', views.Booking_create, name='box_create'),
    path('<int:pk>/box_update', views.Booking_create, name='box_update'),
    path('<int:pk>/box_delete', views.Booking_create, name='box_delete'),
    path('price_create/', views.Booking_create, name='price_create'),
    path('<int:pk>/price_update', views.Booking_create, name='price_update'),
    path('<int:pk>/price_delete', views.Booking_create, name='price_delete'),
    path('schedule_create/', views.Booking_create, name='schedule_create'),
    path('<int:pk>/schedule_update', views.Booking_create, name='schedule_update'),
    path('<int:pk>/schedule_delete', views.Booking_create, name='schedule_delete'),
    path('category_create/', views.Booking_create, name='category_create'),
    path('<int:pk>/category_update/', views.Booking_create, name='category_update'),
    path('<int:pk>/category_delete/', views.Booking_create, name='category_delete'),
    path('history/', views.list_client_booking_history, name='history'),
    path('<int:pk>/delete_booking', views.BookingDeleteView.as_view(), name='delete_booking'),
]
