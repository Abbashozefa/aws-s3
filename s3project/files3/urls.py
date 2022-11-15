from django.urls import path
from django.urls import include
from files3 import views
urlpatterns = [
    
    path('mainpage/', views.page, name='mainpage'),
    path('mainpage2/', views.page2, name='mainpage2')
]