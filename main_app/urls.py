from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gunpla/', views.gunpla_index, name="index"),
    path('about/', views.about, name='about'),
    path('gunpla/create/', views.GunplaCreate.as_view(), name='add_gunpla'),
    path('gunpla/<int:gunpla_id>/', views.gunpla_detail, name='detail'),
    path('gunpla/<int:pk>/update/', views.GunplaUpdate.as_view(), name='gunpla_update'),
    path('gunpla/<int:pk>/delete/', views.GunplaRemove.as_view(), name='gunpla_delete'),
    path('accessories/', views.AccessoriesList.as_view(), name='acc_index'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='add_acc'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='acc_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryRemove.as_view(), name='acc_delete'),
]

