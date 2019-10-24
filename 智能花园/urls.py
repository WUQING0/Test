"""智能花园 URL Configuration

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
from django.urls import path
from huayuan import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'',views.login),
    path(r'login/',views.login),
    path(r'register/',views.register),
    path(r'index/',views.index),
    path(r'invoice/',views.invoice),
    path(r'blank/',views.blank),
    path(r'modals',views.modal),
    path(r'chartjs/',views.chartjs),
    path(r'pepei/',views.pepei),
    path(r'ren/',views.ren),
    path(r'rizhi/',views.rizhi),
    path(r'settings/',views.settings),
    path(r'tabs/',views.tabs),
    path(r'user/',views.user),
    path(r'zhi/',views.user),
    path(r'zhiwuzhonglei/',views.zhiwuzhonglei),
    path(r'progress_bars/',views.progress_bars),
    path(r'aleats/',views.aleats),
    path(r'buttons/',views.buttons),
    path(r'cards/',views.cards),
    path(r'alerts/',views.alerts),
]
