from django.contrib import admin
from django.urls import path
from main.views import *



urlpatterns=[
    path('employee_list',employee_list),
    path('employee_create',employee_create),
    path('attendance_add',attendance_add)
]