"""quero_cultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^agents_indicators', include('agents_indicators.urls')),
    url(r'^library_indicators', include('library_indicators.urls')),
    url(r'^events_indicators', include('events_indicators.urls')),
    url(r'^project_indicators', include('project_indicators.urls')),
    url(r'^museums_indicators', include('museums_indicators.urls')),
    url(r'^space_indicators', include('space_indicators.urls')),
    url(r'^mixed_indicators', include('mixed_indicators.urls')),
    url(r'^new_markers', views.get_last_minutes_markers_json),
]
