from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_ebook, name='publish_ebook'),

]