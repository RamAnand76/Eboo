from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('publish/', views.publish_ebook, name='publish_ebook'),
    path('', views.home, name='home'),
]
