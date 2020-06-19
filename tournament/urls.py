"""data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views
from users import views as users_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.tournament, name='tournament'),
    path('', views.pwl, name='pwl'),
    path('', views.bbl, name='bbl'),
    path('', views.minton, name='minton'),
    path('', views.tennis, name='tennis'),
    path('arm/', views.arm, name='arm'),
    path('plift/', views.plift, name='plift'),
    path('bmint/', views.bmint, name='bmint'),
    path('bbild/', views.bmint, name='bbild'),
path('ten/', views.ten, name='ten'),
path('king/', views.king, name='king'),
    path('new/', views.new, name='new'),
    path('pay/', views.pay, name='pay'),
    #path('', views.ooo, name='ooo'),
]
