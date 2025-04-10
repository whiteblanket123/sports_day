"""
URL configuration for spproject project.

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
from django.conf.urls import handler404
from django.urls import path
from spapp.views import test1d, test2d, test3d, submit_input, input_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1grade/', test1d, name="1grade"),
    path('2grade/', test2d, name="2grade"),
    path('3grade/', test3d, name="3grade"),
    path('input/', submit_input, name="submit_input"),
    path('input_page/', input_page, name= "input_page"),
]

handler404 = 'spapp.views.custom_404_view'
