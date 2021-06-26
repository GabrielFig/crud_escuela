"""crudEscuela URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from crudapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', views.home_alumno, name='index'),
    path('alumnos/<int:pk>/', views.AlumnoDetailView.as_view(), name='detail'),
    path('alumnos/edit/<int:pk>/', views.edit, name='edit'),
    path('alumnos/create/', views.create, name='create'),
    path('alumnos/delete/<int:pk>/', views.delete, name='delete'),
]
