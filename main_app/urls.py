from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gunpla/', views.gunpla_index, name="index"),
    path('about/', views.about, name='about'),
    path('gunpla/<int:gunpla_id>/', views.gunpla_detail, name='detail'),
]

