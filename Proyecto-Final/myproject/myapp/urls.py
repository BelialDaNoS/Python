from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:model_name>/', views.add_data, name='add_data'),
    path('search/', views.search_data, name='search_data'),
]
