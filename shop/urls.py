from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.edition_list, name='edition_list'),
    path('<int:id>/<slug:slug>/', views.edition_detail, name='edition_detail'),
]
