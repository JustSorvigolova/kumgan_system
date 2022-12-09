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
    path('<int:pk>/delete_booking', views.BookingDeleteView.as_view(), name='delete_booking'),
    path('box_create/', views.BoxCreate.as_view(), name='box_create'),
    path('box_list/', views.BoxListView.as_view(), name='box_list'),
    path('<int:pk>/box_update', views.BoxUpdateView.as_view(), name='box_update'),
    path('<int:pk>/box_delete', views.BoxDeleteView.as_view(), name='box_delete'),
    path('price_create/', views.PriceCreateView.as_view(), name='price_create'),
    path('price_list/', views.PriceListView.as_view(), name='price_list'),
    path('<int:pk>/price_update', views.PriceUpdateView.as_view(), name='price_update'),
    path('<int:pk>/price_delete', views.PriceDeleteView.as_view(), name='price_delete'),
    path('schedule_create/', views.ScheduleCreate.as_view(), name='schedule_create'),
    path('schedule_list/', views.ScheduleListView.as_view(), name='schedule_list'),
    path('<int:pk>/schedule_update', views.ScheduleUpdateView.as_view(), name='schedule_update'),
    path('<int:pk>/schedule_delete', views.ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('category_create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/category_update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/category_delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('history/', views.list_client_booking_history, name='history'),
    path('<int:pk>/delete_booking', views.BookingDeleteView.as_view(), name='delete_booking'),
]
