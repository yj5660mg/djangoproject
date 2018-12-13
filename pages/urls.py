from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('seen/<list_id>', views.seen, name='seen'),
    path('notseen/<list_id>', views.notseen, name='notseen'),
    path('edit/<list_id>', views.edit, name='edit'),
]
