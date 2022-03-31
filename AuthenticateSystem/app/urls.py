from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage,name="home"),
    path('login/', views.LoginUser, name="login"),
    path('register/',views.RegisterUser, name="register"),
    path('logout/',views.LogoutUser, name="logout")
]