from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("profile", views.profile, name="profile"),
    path("logout", views.logout, name="logout"),
]