from django.contrib import admin
from django.urls import path ,include
from crud.views import home
from . import views as v


urlpatterns = [
    path('',v.home,name='home'),
    path('save/',v.save_data,name='save'),
    path('delete/',v.delete_data,name='delete'),
    path('edit/',v.edit_data,name='edit')



]
