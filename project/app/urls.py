from django.urls import path,include
from .views import register
from .views import registerdata

from app import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('registerdata/',views.registerdata,name='register')

]