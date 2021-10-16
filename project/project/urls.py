"""project URL Configuration

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
from django.urls import path, re_path

from search import views

# https://docs.djangoproject.com/en/dev/topics/http/urls/#url-dispatcher
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_text/', views.search_text, name='search_text'),
    re_path(r'^search_text/(?P<query>\w+)/$', views.search_text, name='search_text'),
    re_path(r'^search_text/(?P<query>\w+)/(?P<id>\d+)/(?P<action>\w+)/$', views.action, name='search_text'),
]
