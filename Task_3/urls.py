"""
URL configuration for Task_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    # path('', task_list, name='task_list'),
    # path('<int:pk>/', task_detail, name='task_detail'),
    # path('new/', task_new, name='task_new'),
    # path('<int:pk>/edit/', task_edit, name='task_edit'),
    # path('<int:pk>/delete/', task_delete, name='task_delete'),
    path('task_list/',task_list, name='task_list'),

]
