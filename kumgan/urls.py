from django.urls import path
from kumgan import views

app_name = 'kumgan'
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signup, name="signin"),
    path('signout/', views.signout, name="signout"),
]
