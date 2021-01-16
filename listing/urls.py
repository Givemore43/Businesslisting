from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('business_list/', views.business_list, name='business_list'),
    path('list_detail/<int:year>/<int:month>/<int:day>/<slug:listing>/',
         views.list_detail, name='list_detail'),
    path('search/', views.search, name='search'),
]