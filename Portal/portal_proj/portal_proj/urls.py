"""
URL configuration for portal_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from system.views import *

urlpatterns = [
    # path('', user_login, name='home'), 
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('dashboard_view/', dashboard_view, name='dashboard'),
    path('add-admin/', add_admin, name='add_admin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add-admin/', add_admin, name='add_admin'),
    path('users/add/', add_user, name='add_user'),
    path('students/add/', add_student, name='add_student'),
    path('colleges/add/', add_college, name='add_college'),
    path('add_employee/', add_employee, name='add_employee'),
    path('add_manager/', add_manager, name='add_manager'),
    path('emp_dashboard/', emp_dashboard, name="emp_dashboard")

]
